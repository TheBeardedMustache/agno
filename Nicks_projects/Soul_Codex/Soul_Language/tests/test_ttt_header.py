import pytest

from src.ttt import decode_ttt_header, encode_ttt_header


def test_encode_decode_roundtrip():
    for value in (0, 1, 7, 26):
        trits = encode_ttt_header(value)
        assert len(trits) == 3
        header = decode_ttt_header(trits)
        assert header.value == value
        assert header.encode() == trits


def test_specific_values():
    assert encode_ttt_header(0) == "000"
    assert encode_ttt_header(26) == "222"
    assert decode_ttt_header("021").value == 7


def test_invalid_values():
    with pytest.raises(ValueError):
        encode_ttt_header(27)
    with pytest.raises(ValueError):
        decode_ttt_header("0122")
    with pytest.raises(ValueError):
        decode_ttt_header("0a2")
