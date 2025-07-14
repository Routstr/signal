import os
import asyncio
from mcp.server.fastmcp import FastMCP
import aiohttp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

mcp = FastMCP("SignalBot")

# Initialize SignalBot configuration
signal_service_host = os.environ.get("SIGNAL_SERVICE_HOST", "localhost")
signal_service_port = os.environ.get("SIGNAL_SERVICE_PORT", "8080")
signal_id = os.environ.get("SIGNAL_ID")
group_id = os.environ.get("GROUP_ID") # This is the group ID for sending to a group

@mcp.tool()
async def send_signal_message(message: str, recipient: str = None) -> str:
    """Send a message via Signal API directly.
    
    Args:
        message: The message to send.
        recipient: Optional recipient (phone number or group ID). If not provided, sends to default group.
    """
    try:
        url = f"http://{signal_service_host}:{signal_service_port}/v2/send"
        
        payload = {
            "message": message,
            "number": signal_id,
            "recipients": [],
            "text_mode": "styled"
        }

        if recipient:
            payload["recipients"].append(recipient)
        elif group_id:
            payload["recipients"].append(group_id)
        else:
            return "Failed to send message: No recipient or default group ID provided."

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response.raise_for_status() # Raise an exception for bad status codes
                response_text = await response.text()
                return f"Message sent successfully to {payload['recipients']}: {message}. Response: {response_text}"
        
    except aiohttp.ClientError as e:
        return f"Failed to send message: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


if __name__ == "__main__":
    mcp.run()