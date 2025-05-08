import nest_asyncio
nest_asyncio.apply()

import asyncio
import json
from mcp import ClientSession
from mcp.client.sse import sse_client

async def main():
    try:
        # Establish connection to MCP server
        async with sse_client("http://localhost:8050/sse") as connection:
            read, write = connection
            async with ClientSession(read, write) as session:
                await session.initialize()
                print("✅ Successfully connected to MCP Server")

                # Execute web search through MCP protocol
                print("\n🔍 Performing research query...")
                search_result = await session.call_tool("web_search", {
                    "query": "Model context protocol",
                    "max_results": 3
                })

                # Process and display results
                if search_result and search_result.content:
                    result_data = json.loads(search_result.content[0].text)
                    if "results" in result_data:
                        print("\n📊 Search Results Summary:")
                        for idx, result in enumerate(result_data["results"], 1):
                            print(f"\n🌐 Result {idx}:")
                            print(f"📌 Title: {result.get('title', 'No Title')}")
                            print(f"📝 Content: {result.get('content', '')[:150]}...")
                            print(f"🔗 URL: {result.get('url', '')}")
                    else:
                        print("⚠️ No results found in the response")
                else:
                    print("⚠️ Empty response from server")

    except ConnectionRefusedError:
        print("❌ Connection failed - Is the server running?")
    except json.JSONDecodeError as e:
        print(f"❌ Invalid response format: {str(e)}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {str(e)}")

if __name__ == "__main__":
    print("🚀 Starting MCP Client...")
    asyncio.run(main())