"""Demo blockchain CLI."""

from __future__ import annotations

from chain.blockchain import Blockchain
from chain.wallet import Wallet


def main() -> None:
    chain = Blockchain(difficulty=2)
    wallet = Wallet.generate()
    msg = b"hello blockchain"
    sig = wallet.sign(msg)
    block = chain.add_block(
        {
            "message": msg.decode(),
            "signature": sig,
            "public_key": wallet.public_key_hex(),
        }
    )
    print(f"Chain length: {len(chain.chain)}")
    print(f"Latest hash: {block.hash[:16]}...")
    print(f"Valid chain: {chain.is_valid()}")
    print(f"Signature ok: {wallet.verify(msg, sig, wallet.public_key_hex())}")


if __name__ == "__main__":
    main()
