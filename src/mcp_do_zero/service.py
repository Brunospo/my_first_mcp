import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def _get_key(passphrase: str) -> bytes:
    salt = b"static_salt_16bytes"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))


def encrypt(plaintext: str, passphrase: str) -> str:
    fernet = Fernet(_get_key(passphrase))
    return fernet.encrypt(plaintext.encode()).decode()


def decrypt(token: str, passphrase: str) -> str:
    fernet = Fernet(_get_key(passphrase))
    return fernet.decrypt(token.encode()).decode()
