from __future__ import annotations

from enum import IntEnum

from ..ttt import decode_ttt_header, encode_ttt_header


class Opcode(IntEnum):
    """Enumeration of canonical opcodes from Opcode Annex A."""

    NO_OP = 0
    ALU = 1
    BRANCH = 2
    LOAD = 3
    OP_4 = 4
    OP_5 = 5
    OP_6 = 6
    OP_7 = 7
    OP_8 = 8
    OP_9 = 9
    OP_10 = 10
    OP_11 = 11
    OP_12 = 12
    OP_13 = 13
    OP_14 = 14
    OP_15 = 15
    OP_16 = 16
    OP_17 = 17
    OP_18 = 18
    OP_19 = 19
    OP_20 = 20
    OP_21 = 21
    OP_22 = 22
    OP_23 = 23
    DIAG_PING = 24
    OP_24 = 24
    DIAG_STATS = 25
    OP_25 = 25
    DIAG_MIRROR = 26
    OP_26 = 26

    def encode(self) -> str:
        """Return the 3-trit encoding for this opcode."""
        return encode_opcode(self)


def encode_opcode(opcode: Opcode | int) -> str:
    """Encode ``opcode`` into a 3-trit string."""
    if isinstance(opcode, Opcode):
        value = int(opcode)
    else:
        value = int(opcode)
    return encode_ttt_header(value)


def decode_opcode(trits: str) -> Opcode:
    """Decode a 3-trit string into :class:`Opcode`."""
    value = decode_ttt_header(trits).value
    try:
        return Opcode(value)
    except ValueError as exc:
        raise ValueError("invalid opcode") from exc


__all__ = ["Opcode", "encode_opcode", "decode_opcode"]
