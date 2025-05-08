# MCP Research Assistant

A client-server system demonstrating web research capabilities using MCP protocol and Tavily API integration.

## Project Overview

- **Server**: FastMCP server with Tavily API web search tool
- **Client**: Research query interface with formatted results display
- **Port**: 8050 (SSE transport)

## Features

- Web search integration through Tavily API
- Structured result formatting
- Error handling for API calls
- SSE-based client-server communication

## Requirements

`requirements.txt`:
```text
mcp
uvicorn
requests
nest_asyncio
python-dotenv
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Get Tavily API key:
   - Sign up at [tavily.com](https://tavily.com)
   - Replace `TAVILY_API_KEY` in server.py with your actual key

```python
# In server.py
TAVILY_API_KEY = "your_api_key_here"  # Replace with actual key
```

## Usage

### Start Server
```bash
uvicorn server:app --reload
```

### Run Client
```bash
python client.py
```

**Sample Output**:
```
🚀 Starting MCP Client...
✅ Successfully connected to MCP Server

🔍 Performing research query...

📊 Search Results Summary:

🌐 Result 1:
📌 Title: Model Context Protocol Documentation
📝 Content: The Model Context Protocol (MCP) provides a standardized way for AI models to communicate...
🔗 URL: https://example.com/mcp-docs

🌐 Result 2:
📌 Title: Understanding MCP Architecture
📝 Content: Comprehensive guide to Model Context Protocol implementation patterns...
🔗 URL: https://techblog.com/mcp-analysis
```

## Custom Queries

Modify the query parameters in client.py:
```python
search_result = await session.call_tool("web_search", {
    "query": "Latest AI research papers",
    "max_results": 5  # Increase result count
})
```

## Troubleshooting

| Error                        | Solution                                  |
|------------------------------|-------------------------------------------|
| Connection refused           | Verify server is running on port 8050     |
| Invalid API key               | Check Tavily API key in server.py         |
| JSON decode errors           | Ensure Tavily API returns valid response  |
| Timeout errors               | Check network connection to Tavily API    |

Key points to note:
1. Requires valid Tavily API key for search functionality
2. Server uses uvicorn for ASGI support
3. Client includes comprehensive error handling
4. Results are formatted for easy readability
5. System demonstrates real-world API integration pattern with MCP
