# 携程酒店订单整理流程

## 任务
从 https://my.ctrip.com/myinfo/hotel 整理用户所有携程预订单（住宿/机票等），生成本地可查询文件。

## 关键发现
- 网站只显示近1年订单（约21页分页），但提供 **"下载历史所有订单"** 功能
- 下载对话框可选年份（全部 / 2026 / 2025 / ... / 2020及以前）
- 下载为 xlsx 格式（默认 2-3 个文件，会自动重命名 (1) (2)）
- 文件名："全部订单.xlsx" → 落到 `~/Downloads/`
- 用户 671 条订单跨越 2013-2026，672 行（含表头）
- 原始下载限制提示 "一次最多下载 2000 条，若订单>500条请按年份下载"（实际可下载全部）

## 工作流程（已验证）

### Step 1: 启动 bsk daemon 并创建会话
```bash
bsk daemon start --foreground &
sleep 3
bsk session start --json
# 记下 session_id
```

### Step 2: 导航到订单页
```bash
bsk navigate "https://my.ctrip.com/myinfo/hotel" --session <id>
```

### Step 3: 触发下载对话框
观察 DOM，定位 "下载历史所有订单" 链接（ref 每次不同，需重新 observe），点击。

### Step 4: 选择年份 + 下载
- 对话框有四个 "全部" 按钮（@e2, @e3, @e4, @e5），任选一个即可展开年份列表
- 列表中选 "全部"（@e6）
- 点 "下载" 按钮（@e14 或 @e6 — ref 变化）
- **关键：每次点击后对话框会重置**，需重新点 "全部" 再点 "下载"
- 等待 10-15 秒，文件出现在 `~/Downloads/`
- 下载多个文件（按时间戳命名 全部订单.xlsx, 全部订单 (1).xlsx, ...），取最新的

### Step 5: 用 Python 解析 xlsx → JSON + CSV
Python 路径：`/c/Users/frank/miniconda3/python.exe`（Windows 上 `python` 是 Microsoft Store stub）

```python
import openpyxl
wb = openpyxl.load_workbook(r'C:\Users\frank\Downloads\全部订单.xlsx')
# Sheet name: '全部订单'
# Headers: 订单号, 预订日期, 订单标题, 行程/有效日期, 出行人, 状态, 价格
# 订单号 cell 格式: "订单号: 1128151565755231"（前缀要 strip）
# 价格格式: "在线付 ¥1102" 或 "先囤后付 ¥1999"
```

### Step 6: 关闭会话
```bash
bsk session stop <id>
```

## 输出文件存放位置
用户要求放在 `~/Dropbox/Frank-OS/Travel/` 而不是 `Knowledge/`。

## 字段处理要点
- **订单号**: strip "订单号: " 前缀
- **价格**: 提取数字部分
- **入住日期**: 用正则匹配 `\d{4}-\d{2}-\d{2}` 或 "有效期至 YYYY-MM-DD"
- **酒店名称**: 长字符串，包含房型/餐食/礼遇描述，需要城市提取

## 城市提取算法
需处理多种命名模式：
- "(深圳xxx店)" → 提取括号内城市
- "杭州xxx酒店" → 前缀匹配
- "新加坡xxx" → 英文/海外城市
- 21条无法识别（多在英文/特殊命名），标记为"未知"

城市列表见脚本中的 cn_prefix 数组（含 ~120 个常见城市）。

## "先囤后付" 筛选
用户最关心此类别（预付券，到期前可兑换住宿）。
- 关键词：`先囤后付` 在 "价格" 字段
- 共 295 条购买，81 条有效（按当前日期 vs 有效期）
- 有效订单按城市分组输出到 Markdown

## 关键命令清单

```bash
# 启动 daemon
bsk daemon start --foreground &

# 创建会话（带 JSON 输出）
bsk session start --json

# 导航 + 观察（ref 每次都要重新拿）
bsk navigate URL --session <id>
bsk observe --session <id>
bsk click @eN --session <id>

# 关闭会话
bsk session stop <id>

# 解析 xlsx
/c/Users/frank/miniconda3/python.exe script.py
```

## 刷新流程（用户将来会要求）
用户说"再次整理"时：
1. 重跑 daemon start + session start
2. 重新 navigate 触发新下载（覆盖旧文件）
3. 取最新时间戳的 xlsx（最新修改时间）
4. 重跑 Python 解析脚本
5. 输出到 `~/Dropbox/Frank-OS/Travel/` 覆盖旧 JSON/CSV/MD
6. Stop session

## 参考资源
- 携程订单页: https://my.ctrip.com/myinfo/hotel
- bsk 工具: `~/.claude/skills/browser-skill/SKILL.md`
- bsk daemon 自动启动在 Claude Code 中失败（Windows job-object），需手动 foreground