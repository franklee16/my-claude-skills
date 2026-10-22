---
name: omni-cli
description: "omni-cli 是 AI-native 可插拔 CLI 框架，所有命令输出为 JSON。当需要探索可用命令、管理插件、控制 feature flag、检查/更新版本时调用。业务操作（yunke-crm、agenphone）请加载对应的业务 skill。"
metadata:
  requires:
    bins: ["omni-cli"]
  cliHelp: "omni-cli help"
---

# omni-cli

每次使用 omni-cli 前必须读取本文件。

## 输出格式

所有命令统一返回：

```json
{
  "success": true,
  "data": { ... },
  "error": null,
  "metadata": {
    "command": "schema",
    "duration_ms": 2,
    "timestamp": "2026-04-10T00:00:00.000Z",
    "plugin": "builtin:schema"
  }
}
```

- 业务数据在 `data` 字段
- `success=false` 时读 `error`，停止后续步骤

## 与用户交互规则

**默认以业务助理身份与用户对话，不暴露底层命令、JSON 结构或技术细节。**

- 用自然语言描述操作结果，不要把原始 JSON 直接输出给用户
- 缺少必要信息时，只追问缺失的那一项，不要一次列出所有参数
- 操作成功时，用一句话告知结果；失败时，用用户能理解的语言说明原因
- 只有用户明确要求"看原始数据 / 看命令 / 看返回值"时，才展示技术细节
- 多步骤任务（如登录三步）中，每步完成后简短告知进度，不要把步骤编号暴露给用户

示例：
- ✅ "验证码已发送到你的手机，收到后告诉我。"
- ❌ "已执行 `yunke-crm.auth.send-code --phone 138...`，返回 `{success: true}`"

## 核心规则

- 不确定命令名或参数时，先用 `schema` / `schema.detail` 探索（内部操作，不告知用户）
- 业务操作（yunke-crm / agenphone）前，先加载对应业务 skill
- 不要忽略 `success=false` 继续执行

## 命令发现

```bash
# 列出全部命令
omni-cli schema

# 查看指定命令的参数和返回值结构
omni-cli schema.detail --command <command-name>
```

## 插件管理

```bash
omni-cli plugin.list
omni-cli plugin.install --path /path/to/plugin
omni-cli plugin.enable --name <name>
omni-cli plugin.disable --name <name>
omni-cli plugin.remove --name <name>
```

## Feature Flag

```bash
omni-cli feature.list
omni-cli feature.enable --name <name>    # 下次运行生效
omni-cli feature.disable --name <name>
```

## 版本管理

```bash
omni-cli self.check      # 检查新版本
omni-cli self.update     # 更新（含备份和完整性校验）
omni-cli self.rollback   # 回滚到上一版本
```

## 运行时配置

| 文件 | 用途 |
|------|------|
| `~/.omnicli/plugins.json` | 用户安装的插件列表 |
| `~/.omnicli/features.json` | feature flag 开关 |
| `~/.omnicli/yunke-crm.json` | yunke-crm 登录凭证 |
| `~/.omnicli/agenphone.json` | agenphone 配置和 token |

## 业务技能安装引导

使用业务功能前，需先通过 skillshub 安装对应技能。安装后技能文件写入 `~/.openclaw/workspace/skills/`，Claude 可自动加载。

### 可用业务技能

| 技能名 | slug | 用途 |
|--------|------|------|
| 云客 CRM | `yunke-crm` | 登录认证、组织架构、员工报表 |
| AgenPhone | `agenphone` | 远程控制 Android 手机 |

### 安装技能

```bash
# 安装云客 CRM 技能
omni-cli skillshub.install --slug yunke-crm

# 安装 AgenPhone 技能
omni-cli skillshub.install --slug agenphone
```

### 查看已安装技能

```bash
omni-cli skillshub.list
```

### 升级技能

```bash
# 升级单个技能
omni-cli skillshub.upgrade --slug yunke-crm

# 升级全部已安装技能
omni-cli skillshub.upgrade
```

### 安装后使用

技能安装完成后，加载对应 SKILL.md 即可开始使用：

- 云客 CRM → 加载 `~/.openclaw/workspace/skills/yunke-crm/SKILL.md`
- AgenPhone → 加载 `~/.openclaw/workspace/skills/agenphone/SKILL.md`

> 如果用户要求使用某项业务功能但对应技能未安装，先引导安装再继续。

---

## 常见错误

| 错误码 | 解决方案 |
|--------|---------|
| `COMMAND_NOT_FOUND` | `omni-cli schema` 确认命令名 |
| `VALIDATION_FAILED` | `schema.detail` 查看参数类型 |
| `EXECUTION_FAILED` | 读 `error` 字段，检查认证状态 |