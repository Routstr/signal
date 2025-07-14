#!/usr/bin/env python3
"""
Test script to test the MCP server functionality
"""
import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the MCP server by calling the send_signal_message tool"""
    
    # Server parameters - run the mcp_server.py script
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"],
        env=None
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the session
                await session.initialize()
                
                # List available tools
                tools = await session.list_tools()
                print("Available tools:")
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")
                
                # Test the send_signal_message tool
                print("\nTesting send_signal_message tool...")
                
                result = await session.call_tool(
                    "send_signal_message",
                    arguments={
                        "message": "Test message from MCP client!"
                    }
                )
                
                print(f"Result: {result.content}")
                
    except Exception as e:
        print(f"❌ Error testing MCP server: {str(e)}")
        print(f"Error type: {type(e).__name__}")

if __name__ == "__main__":
    print("Testing MCP Signal server...")
    asyncio.run(test_mcp_server())