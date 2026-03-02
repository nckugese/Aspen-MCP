# Aspen Plus MCP Integration

Control Aspen Plus simulations via the Model Context Protocol (MCP).

See [aspen-mcp/README.md](aspen-mcp/README.md) for full documentation on available tools and block/stream reference.

## Prerequisites

- Windows (Aspen Plus only runs on Windows)
- Aspen Plus installed
- Python 3.11+

## Setup

1. Install dependencies:

   ```bash
   pip install -r aspen-mcp/requirements.txt
   ```

2. Copy `.mcp.json.example` to `.mcp.json`:

   ```bash
   cp .mcp.json.example .mcp.json
   ```

3. Edit `.mcp.json` and update the path to `server.py`:

   ```json
   {
     "mcpServers": {
       "aspen-plus": {
         "command": "python",
         "args": ["path/to/aspen-mcp/server.py"]
       }
     }
   }
   ```

   If `python` is not in your system PATH, use the full path to your Python executable:

   ```json
   "command": "C:/Users/YourName/AppData/Local/Programs/Python/Python311/python.exe"
   ```

## License

This project is licensed under the MIT License.
