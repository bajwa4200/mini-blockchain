from chain.blockchain import Blockchain


def test_genesis_and_add_block():
    chain = Blockchain(difficulty=1)
    assert len(chain.chain) == 1
    block = chain.add_block({"msg": "hi"})
    assert block.index == 1
    assert chain.is_valid()


def test_tampered_chain_invalid():
    chain = Blockchain(difficulty=1)
    chain.add_block({"msg": "a"})
    chain.chain[1].data = {"msg": "tampered"}
    assert not chain.is_valid()
