from mcp.server.fastmcp import FastMCP, Context
import requests
from typing import Dict, Any

TAVILY_API_KEY = "Tavily-api-key"

mcp = FastMCP(
    name="Research Assistant",
    host="0.0.0.0",
    port=8050,
    cors_allowed_origins=["*"]
)

@mcp.tool()
async def web_search(ctx: Context, query: str, max_results: int = 5) -> Dict[str, Any]:
    """Web search using Tavily API"""
    response = requests.post(
        "https://api.tavily.com/search",
        json={"query": query, "api_key": TAVILY_API_KEY, "max_results": max_results},
        timeout=10
    )
    return response.json()



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(mcp.sse_app(), host="0.0.0.0", port=8050)
