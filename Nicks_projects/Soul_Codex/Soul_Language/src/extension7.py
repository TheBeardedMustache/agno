"""Run-length text encoding for SIL extension 7."""

from __future__ import annotations

from dataclasses import dataclass


_DELIMITER = "#"


@dataclass(frozen=True, slots=True)
class RLEText:
    """Dataclass representing RLE encoded text for extension 7."""

    text: str

    def encode(self) -> str:
        return encode_rle(self.text)


def encode_rle(text: str) -> str:
    """Encode ``text`` using a simple run-length scheme.

    Sequences of repeated characters are replaced by ``<char>#<count>`` when
    ``count`` is greater than one. Digits that appear in the original text are
    preserved because counts are always prefixed by ``#``.
    """
    if not text:
        return ""

    result = []
    current = text[0]
    count = 1
    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result.append(current)
            if count > 1:
                result.append(f"{_DELIMITER}{count}")
            current = ch
            count = 1
    result.append(current)
    if count > 1:
        result.append(f"{_DELIMITER}{count}")
    return "".join(result)


def decode_rle(data: str) -> RLEText:
    """Decode a run-length encoded string ``data`` into :class:`RLEText`."""
    if not data:
        return RLEText("")

    result = []
    i = 0
    n = len(data)
    while i < n:
        ch = data[i]
        i += 1
        count = 1
        if i < n and data[i] == _DELIMITER:
            i += 1
            j = i
            while j < n and data[j].isdigit():
                j += 1
            if j == i:
                raise ValueError("missing digits after delimiter")
            count = int(data[i:j])
            i = j
        result.append(ch * count)
    return RLEText("".join(result))
