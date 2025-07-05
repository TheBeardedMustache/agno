from src.sil.frame import Frame
from src.sil.opcode import Opcode
from src.ntru import generate_keypair


def test_sign_verify_positive():
    pub, priv = generate_keypair()
    frame = Frame(ttt=1, window=1, qos=1, opcode=Opcode.NO_OP)
    frame.sign(priv, "run")
    assert frame.verify(pub)


def test_sign_verify_bitflip_fail():
    pub, priv = generate_keypair()
    frame = Frame(ttt=2, window=2, qos=2, opcode=Opcode.NO_OP)
    frame.sign(priv, "op")
    # flip one bit in signature
    sig = bytearray(frame.sig_lattice.signature)
    sig[0] ^= 0x01
    frame.sig_lattice.signature = bytes(sig)
    assert not frame.verify(pub)


def test_sign_verify_wrong_intent():
    pub, priv = generate_keypair()
    frame = Frame(ttt=3, window=3, qos=0, opcode=Opcode.NO_OP)
    frame.sign(priv, "alpha")
    # replace intent code with that of another intent
    frame.sig_lattice.intent_code = Frame.intent_code("beta")
    assert not frame.verify(pub)
