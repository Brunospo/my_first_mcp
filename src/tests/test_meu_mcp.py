import pytest
from mcp.client.client import Client

from mcp_do_zero.meu_mcp import server


@pytest.fixture
async def mcp_session():

    async with Client(server) as client:
        yield client


async def helper_encrypt(session, message, key):
    result = await session.call_tool(
        "encrypt_message",
        arguments={"message": message, "encryption_key": key},
    )

    return result


async def helper_decrypt(session, encrypted_message, key):
    result = await session.call_tool(
        "decrypt_message",
        arguments={"encrypted_message": encrypted_message, "encryption_key": key},
    )

    return result


@pytest.mark.anyio
async def testar_encrypt_message(mcp_session):
    """Testar a tool de encrypt_message"""
    result = await helper_encrypt(
        mcp_session, message="Hello world", key="my_super_key"
    )
    assert len(result.structured_content["result"]) > 60


@pytest.mark.anyio
async def testar_decrypt_message(mcp_session):
    """Testar a tool de decrypt_message"""
    key = "secret_key"
    message = "heeeey"
    encrypt_result = await helper_encrypt(mcp_session, message=message, key=key)
    encrypted_message = encrypt_result.structured_content["result"]

    decrypt_result = await helper_decrypt(
        mcp_session, encrypted_message=encrypted_message, key=key
    )

    assert decrypt_result.structured_content["result"] == message
