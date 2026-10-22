# WRDS MCP quick reference (this machine)

Local setup notes; the upstream full guide (`install/wrds-mcp.md`) was not copied to this machine. Machine-wide details live in `~/.claude/CLAUDE.md` (Environment section).

## Your credentials (required)

```bash
# on this machine, already in ~/.wrds-mcp.env (tunnel) and ~/.claude.json (MCP server)
export WRDS_USERNAME="your_wrds_username"   # from WRDS account registration
export WRDS_PASSWORD="your_wrds_password"   # never commit or share
```

## Session startup

```bash
source ~/.wrds-mcp.env && bash ~/barrios-skills/mcp/wrds-mcp/tunnel/tunnel_up.sh
# approve the Duo Push on your phone within ~30s — only run while present
# auth failure exits without retrying (Duo lockout guard, patched 2026-10-05)
```

## MCP env (Cursor / Claude)

```json
{
  "WRDS_USERNAME": "your_wrds_username",
  "WRDS_PASSWORD": "your_wrds_password",
  "WRDS_TUNNEL_PORT": "49600"
}
```

## Shutdown / status

```bash
bash ~/barrios-skills/mcp/wrds-mcp/tunnel/tunnel_down.sh
bash ~/barrios-skills/mcp/wrds-mcp/tunnel/tunnel_status.sh
```
