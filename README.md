# Signal MCP Server

This MCP server provides a tool to send messages via Signal using the existing SignalBot infrastructure.

## Setup
1. First, you need to have signal-cli running locally and have it signed in with your signal account: 
(Make sure you have docker installed)
- Run: 
   ```bash
   cd signal
   chmod +x run_signal_cli.sh
   ./run_signal_cli.sh
   ```
- Choose 1 to run setup
then go to this link and link new device using your signal mobile app: http://127.0.0.1:8080/v1/qrcodelink?device_name=local

- Run the bash script again and choose 2 to have your signal-cli running. 
(Note: You need to use docker ps and docker kill <container> to shut it down as it is running in detached mode)
   ```bash
   ./run_signal_cli.sh
   ```

2. Make sure you have the required dependencies installed:
(We recommend uv for managing dependencies, install it from [here](https://docs.astral.sh/uv/getting-started/installation/))
   ```bash
   uv sync
   ```

3. Ensure your `.env` file contains the required Signal configuration:
Groups and contacts your bot to listen to your "hey goose" command
   ```
   SIGNAL_SERVICE=127.0.0.1:8080
   SIGNAL_ID=+your_phone_number
   GROUP_NAMES=group_name1,bitcoin core
   CONTACTS=+1124234355,+420121434534
   ```

4. Finally, change `path/to/signal` in routstr_management.yaml to your actual path to this current directory. You can further modify the model and instructions in the same file to your liking. 

## Testing

Before using with Claude Desktop, you can test the functionality:

### 1. Test Signal Bot Directly

Run the direct test script to verify your Signal bot configuration:

```bash
cd signal/tests
python test_signal.py
```

This will:
- Load your environment variables
- Show your configuration
- Send a test message to your configured group
- Report success or failure

### 2. Test MCP Server

Test the MCP server functionality:

```bash
cd signal/tests
python test_mcp_client.py
```

This will:
- Start the MCP server
- List available tools
- Call the `send_signal_message` tool
- Show the result

## Running the MCP Server

To start the MCP server:

```bash
python mcp_server.py
```

## Available Tools

### send_signal_message

Send a message via Signal bot.

**Parameters:**
- `message` (required): The message to send
- `recipient` (optional): Phone number or group ID. If not provided, sends to the default group configured in environment variables.

**Examples:**
- Send to default group: `send_signal_message("Hello from MCP!")`
- Send to specific recipient: `send_signal_message("Hello!", "+1234567890")`

## Integration

To use this MCP server with other applications, configure your MCP client to connect to this server. The server provides the `send_signal_message` tool that can be called to send messages through Signal.

## Claude Desktop Integration

To add this MCP server to Claude Desktop:

1. **Locate your Claude Desktop configuration file:**
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Add the server configuration:**
   ```json
   {
     "mcpServers": {
       "signal-bot": {
         "command": "python",
         "args": ["mcp_server.py"],
         "cwd": "/path/to/folder/signal"
       }
     }
   }
   ```

3. **Restart Claude Desktop** for the changes to take effect.

4. **Verify the connection:** You should see the Signal MCP server listed in Claude Desktop's MCP servers section.

## Usage in Claude Desktop

Once connected, you can use the tool in Claude Desktop like this:

- "Send a Signal message saying 'Hello from Claude!' to the default group"
- "Send 'Meeting in 10 minutes' via Signal to +1234567890"

The tool will automatically use your configured Signal bot settings from the `.env` file.

**Note:** Make sure your Signal service is running and accessible at the configured `SIGNAL_SERVICE` address before using the MCP server.
