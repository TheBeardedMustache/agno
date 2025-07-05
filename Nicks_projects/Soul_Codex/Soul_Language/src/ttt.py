"""Ternary Typed Token header parser and encoder.

A TTT header is a 3-trit (base-3 digit) sequence representing a small
integer from 0 to 26 inclusive.  The parser converts the trit string
into an integer value while the encoder performs the inverse
operation.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TTTHeader:
    """Dataclass representing a decoded TTT header."""

    value: int

    def encode(self) -> str:
        """Return the 3-trit encoding for this header."""
        return encode_ttt_header(self.value)


def encode_ttt_header(value: int) -> str:
    """Encode an integer ``value`` into a 3-trit string.

    Parameters
    ----------
    value:
        Integer in the range [0, 27).

    Returns
    -------
    str
        Three-character string where each character is ``'0'``, ``'1'``
        or ``'2'`` representing a single trit.
    """
    if not 0 <= value < 27:
        raise ValueError("TTT value must be between 0 and 26 inclusive")

    trits = []
    for _ in range(3):
        value, rem = divmod(value, 3)
        trits.append(str(rem))
    return "".join(reversed(trits))


def decode_ttt_header(trits: str) -> TTTHeader:
    """Decode a 3-trit string into a :class:`TTTHeader`.

    Parameters
    ----------
    trits:
        Three-character string of digits ``'0'``, ``'1'`` or ``'2'``.

    Returns
    -------
    TTTHeader
    """
    if len(trits) != 3 or any(ch not in "012" for ch in trits):
        raise ValueError("TTT header must be three trits")

    value = 0
    for ch in trits:
        value = value * 3 + int(ch)
    return TTTHeader(value)
