# Mini Blockchain

A teaching-sized proof-of-work blockchain with SHA-256 block hashes and Ed25519 wallets for signing messages. Blocks link through previous hashes; mining difficulty is configurable.

## Quick start

```bash
pip install -e ".[dev]"
mini-blockchain
```

## Tests

```bash
python -m pytest -q
```

## Layout

```
mini-blockchain/
├── chain/
│   ├── hashing.py
│   ├── block.py
│   ├── blockchain.py
│   ├── wallet.py
│   └── cli.py
└── tests/
```

## License

MIT — see [LICENSE](LICENSE).
