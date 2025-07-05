from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Union


TRIT_CHARS = {"-": -1, "0": 0, "+": 1}


class TritError(ValueError):
    """Raised when an invalid trit is encountered."""


TritLike = Union[int, str]


def _normalize_trits(trits: Iterable[TritLike]) -> List[int]:
    result = []
    for t in trits:
        if isinstance(t, str):
            if t not in TRIT_CHARS:
                raise TritError(f"invalid trit character: {t}")
            result.append(TRIT_CHARS[t])
        else:
            if t not in (-1, 0, 1):
                raise TritError(f"invalid trit value: {t}")
            result.append(t)
    return result


def _trits_to_int(trits: Sequence[int]) -> int:
    value = 0
    for t in trits:
        value = value * 3 + (t + 1)
    return value


def _int_to_trits(value: int, width: int) -> List[int]:
    if value < 0 or value >= 3**width:
        raise ValueError(f"value {value} does not fit in {width} trits")
    digits = [0] * width
    remaining = value
    for i in range(width - 1, -1, -1):
        digits[i] = (remaining % 3) - 1
        remaining //= 3
    return digits


@dataclass(slots=True)
class TernaryTypedToken:
    """Represents a TTT extension encoded in three trits."""

    value: int

    @classmethod
    def decode(cls, trits: Sequence[TritLike]) -> "TernaryTypedToken":
        data = _normalize_trits(trits)
        if len(data) != 3:
            raise ValueError("TTT requires exactly 3 trits")
        return cls(value=_trits_to_int(data))

    def encode(self) -> List[int]:
        return _int_to_trits(self.value, 3)


@dataclass(slots=True)
class DeltaTQoS:
    """Represents Δt window and QoS class encoded in four trits."""

    window: int
    qos: int

    @classmethod
    def decode(cls, trits: Sequence[TritLike]) -> "DeltaTQoS":
        data = _normalize_trits(trits)
        if len(data) != 4:
            raise ValueError("Δt/QoS requires exactly 4 trits")
        window = _trits_to_int(data[:3])
        qos = data[3] + 1
        return cls(window=window, qos=qos)

    def encode(self) -> List[int]:
        trits = _int_to_trits(self.window, 3)
        if self.qos not in (0, 1, 2):
            raise ValueError("QoS must be 0, 1, or 2")
        trits.append(self.qos - 1)
        return trits


__all__ = [
    "TernaryTypedToken",
    "DeltaTQoS",
]
