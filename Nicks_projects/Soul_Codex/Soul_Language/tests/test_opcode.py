import pytest
from src.sil.opcode import Opcode, encode_opcode, decode_opcode
from src.sil.frame import Frame


def test_opcode_roundtrip():
    samples = [
        Opcode.NO_OP,
        Opcode.ALU,
        Opcode.BRANCH,
        Opcode.LOAD,
        Opcode.OP_26,
    ]
    for op in samples:
        encoded = encode_opcode(op)
        assert len(encoded) == 3
        decoded = decode_opcode(encoded)
        assert decoded == op
        assert encode_opcode(decoded) == encoded


def test_invalid_opcode_values():
    with pytest.raises(ValueError):
        encode_opcode(27)
    with pytest.raises(ValueError):
        decode_opcode("0122")
    with pytest.raises(ValueError):
        decode_opcode("0a0")


def test_frame_with_opcode():
    frame = Frame(ttt=5, window=4, qos=2, opcode=Opcode.ALU)
    encoded = frame.encode()
    assert len(encoded) == 18
    decoded = Frame.decode(encoded)
    assert decoded == frame
