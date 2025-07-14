#!/usr/bin/env python3
"""
Test script to send a Signal message directly without MCP
"""
import os
import aiohttp
from dotenv import load_dotenv

async def test_send_message():
    # Load environment variables
    load_dotenv()
    
    # Get configuration from environment
    signal_service_host = os.environ.get("SIGNAL_SERVICE_HOST", "localhost")
    signal_service_port = os.environ.get("SIGNAL_SERVICE_PORT", "8080")
    phone_number = os.environ.get("SIGNAL_ID")
    group_recipient = os.environ.get("GROUP_ID") # From curl example
    
    message_text = "Test via Signal API!" # From curl example
    
    url = f"http://{signal_service_host}:{signal_service_port}/v2/send"
    payload = {
        "message": message_text,
        "number": phone_number,
        "recipients": [group_recipient]
    }
    
    print(f"\nSending message: '{message_text}'")
    print(f"To URL: {url}")
    print(f"With payload: {payload}")
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response.raise_for_status() # Raise an exception for bad status codes
                print(f"✅ Message sent successfully! Status: {response.status}")
                print(f"Response: {await response.text()}")
                
    except aiohttp.ClientError as e:
        print(f"❌ Failed to send message: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Testing Signal message sending via direct HTTP request...")
    import asyncio
    asyncio.run(test_send_message())