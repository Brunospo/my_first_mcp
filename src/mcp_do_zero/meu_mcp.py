from mcp.server.mcpserver import MCPServer

from mcp_do_zero.service import decrypt, encrypt

server = MCPServer("Meu Servidor MCP")


@server.tool()
async def encrypt_message(message: str, encryption_key: str) -> str:
    """encrypt a message."""
    try:
        encrypted_message = encrypt(message, encryption_key)
        return encrypted_message
    except Exception as exc:
        return {
            "isError": True,
            "content": [
                {
                    "type": "text",
                    "text": f"Failed to encrypt message! Check if the message and encryption key are correct. Error details: {exc}",
                }
            ],
        }


@server.tool()
async def decrypt_message(encrypted_message: str, encryption_key: str) -> str:
    """decrypt message."""
    try:
        decrypted_message = decrypt(encrypted_message, encryption_key)
        return decrypted_message
    except Exception as exc:
        return {
            "isError": True,
            "content": [
                {
                    "type": "text",
                    "text": f"Failed to decrypt message! Check if the encrypted message and encryption key are correct. Error details: {exc}",
                }
            ],
        }
