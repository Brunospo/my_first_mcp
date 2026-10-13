from pydantic import BaseModel, Field


class InputEncryptSchema(BaseModel):
    encryptedMessage: str = Field(
        description="The encrypted message (format: iv:ciphertext)"
    )
    encryptionKey: str = Field(description="The same passphrase used during encryption")


class OutputEncryptSchema(BaseModel):
    decryptedMessage: str = Field(description="The decrypted plain-text message")
