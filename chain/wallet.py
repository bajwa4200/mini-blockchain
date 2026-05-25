"""Ed25519 wallet for signing messages."""

from __future__ import annotations

import base64
from dataclasses import dataclass

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat


@dataclass
class Wallet:
    private_key: Ed25519PrivateKey

    @classmethod
    def generate(cls) -> Wallet:
        return cls(Ed25519PrivateKey.generate())

    @property
    def public_key(self) -> Ed25519PublicKey:
        return self.private_key.public_key()

    def public_key_hex(self) -> str:
        raw = self.public_key.public_bytes(Encoding.Raw, PublicFormat.Raw)
        return raw.hex()

    def sign(self, message: bytes) -> str:
        sig = self.private_key.sign(message)
        return base64.b64encode(sig).decode()

    @staticmethod
    def verify_signature(message: bytes, signature_b64: str, public_key_hex: str) -> bool:
        try:
            pub = Ed25519PublicKey.from_public_bytes(bytes.fromhex(public_key_hex))
            sig = base64.b64decode(signature_b64)
            pub.verify(sig, message)
            return True
        except Exception:
            return False

    def verify(self, message: bytes, signature_b64: str, public_key_hex: str) -> bool:
        return self.verify_signature(message, signature_b64, public_key_hex)
