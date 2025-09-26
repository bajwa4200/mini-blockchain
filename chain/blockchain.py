"""Proof-of-work blockchain."""

from __future__ import annotations

from dataclasses import dataclass, field

from chain.block import Block, create_genesis


@dataclass
class Blockchain:
    difficulty: int = 2
    chain: list[Block] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.chain:
            self.chain.append(create_genesis())

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, data: dict, mine: bool = True) -> Block:
        block = Block(
            index=len(self.chain),
            timestamp=self.last_block.timestamp + 1,
            data=data,
            previous_hash=self.last_block.hash,
        )
        if mine:
            block.mine(self.difficulty)
        else:
            block.hash = block.compute_hash()
        self.chain.append(block)
        return block

    def is_valid(self) -> bool:
        prefix = "0" * self.difficulty
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.previous_hash != previous.hash:
                return False
            if current.hash != current.compute_hash():
                return False
            if not current.hash.startswith(prefix):
                return False
        return True
