from mcp.server.mcpserver import MCPServer

from app.config import settings
from app.payments import build_mcp_paywall

mcp = MCPServer("resurrection")
paid = build_mcp_paywall(settings.price_private_run)


@mcp.tool()
@paid
async def commission_run(question: str) -> dict:
    """Commission a private analysis run on public aging datasets."""
    return {"status": "not_built"}


@mcp.tool()
async def current_question() -> dict:
    """The aging question the scientist is working on right now."""
    return {"status": "not_built"}


@mcp.tool()
async def findings() -> dict:
    """Public findings with links to code and notebooks."""
    return {"status": "not_built"}
