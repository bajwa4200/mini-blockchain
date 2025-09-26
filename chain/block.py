"""Block structure and mining."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Any

from chain.hashing import hash_payload


@dataclass
class Block:
    index: int
    timestamp: float
    data: dict[str, Any]
    previous_hash: str
    nonce: int = 0
    hash: str = ""

    def payload(self) -> dict[str, Any]:
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }

    def compute_hash(self) -> str:
        return hash_payload(self.payload())

    def mine(self, difficulty: int) -> None:
        prefix = "0" * difficulty
        while True:
            self.hash = self.compute_hash()
            if self.hash.startswith(prefix):
                return
            self.nonce += 1


def create_genesis() -> Block:
    block = Block(
        index=0,
        timestamp=time.time(),
        data={"message": "genesis"},
        previous_hash="0" * 64,
    )
    block.hash = block.compute_hash()
    return block
