import sys

from mcp_do_zero.meu_mcp import server

if __name__ == "__main__":
    try:
        print("Encrypt MCP Server running on stdio...")
        server.run(transport="stdio")
    except Exception as error:
        print(f"Fatal error in main(): {error}", file=sys.stderr)
        sys.exit(1)
