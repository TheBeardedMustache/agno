from src.sil.diag import MirrorMode, handle_diag_opcode, ContextTLV, decode_tlv
from src.sil.frame import encode_mirror_mode, decode_mirror_mode
from src.sil.opcode import Opcode


def test_mirror_mode_roundtrip():
    for state in (True, False):
        encoded = encode_mirror_mode(state)
        assert decode_mirror_mode(encoded) is state


def test_ring_buffer_ttl_purge():
    mm = MirrorMode(size=3, ttl=2, enabled=True)
    mm.record("a")
    mm.tick()
    mm.record("b")
    mm.tick()  # 'a' should expire
    assert list(mm.contents()) == ["b"]


def test_diag_ping_sequence():
    assert handle_diag_opcode(Opcode.DIAG_PING) == Opcode.DIAG_STATS
    assert handle_diag_opcode(Opcode.NO_OP) is None


def test_tlv_roundtrip():
    tlv = ContextTLV(1, b"MRI")
    encoded = tlv.encode()
    decoded, rest = decode_tlv(encoded)
    assert rest == b""
    assert decoded == tlv
