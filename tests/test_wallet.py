from chain.wallet import Wallet


def test_sign_and_verify():
    w = Wallet.generate()
    msg = b"test message"
    sig = w.sign(msg)
    assert w.verify(msg, sig, w.public_key_hex())


def test_invalid_signature():
    w = Wallet.generate()
    assert not w.verify(b"other", w.sign(b"x"), w.public_key_hex())
