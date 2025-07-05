import pytest
from src.sil.frame import (
    Frame,
    decode_delta_t_qos,
    encode_delta_t_qos,
    decode_ttt_header,
    encode_ttt_header,
)
from src.sil.ethics import FrameEthicsError
from src.sil.opcode import Opcode


def test_ttt_roundtrip():
    for value in (0, 1, 13, 26):
        encoded = encode_ttt_header(value)
        assert len(encoded) == 3
        header = decode_ttt_header(encoded)
        assert header.value == value
        assert encode_ttt_header(header.value) == encoded


def test_delta_t_qos_roundtrip():
    for window in range(9):
        for qos in range(3):
            encoded = encode_delta_t_qos(window, qos)
            assert len(encoded) == 3
            decoded = decode_delta_t_qos(encoded)
            assert (decoded.window, decoded.qos) == (window, qos)
            assert decoded.encode() == encoded


def test_frame_encode_decode():
    frame = Frame(ttt=5, window=4, qos=2, opcode=Opcode.NO_OP)
    encoded = frame.encode()
    assert len(encoded) == 18
    decoded = Frame.decode(encoded)
    assert decoded == frame


def test_frame_validate():
    frame = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP)
    frame.validate()  # should not raise

    bad = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP, eer_code=1)
    with pytest.raises(FrameEthicsError):
        bad.validate()
