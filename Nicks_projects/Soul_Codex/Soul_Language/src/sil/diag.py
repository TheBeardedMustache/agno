from __future__ import annotations

import collections
from dataclasses import dataclass, field
from typing import Deque, Iterable, Tuple

from .opcode import Opcode


@dataclass(slots=True)
class MirrorMode:
    """Diagnostic ring buffer with TTL based purge."""

    size: int = 8
    ttl: int = 3
    enabled: bool = False
    _buffer: Deque[Tuple[str, int]] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._buffer = collections.deque(maxlen=self.size)

    def enable(self) -> None:
        self.enabled = True

    def disable(self) -> None:
        self.enabled = False

    def record(self, payload: str) -> None:
        if not self.enabled:
            return
        self._buffer.append((payload, self.ttl))

    def tick(self) -> None:
        new: Deque[Tuple[str, int]] = collections.deque(maxlen=self.size)
        for payload, ttl in self._buffer:
            if ttl > 1:
                new.append((payload, ttl - 1))
        self._buffer = new

    def contents(self) -> Iterable[str]:
        return [payload for payload, _ in self._buffer]


# --- Diagnostic opcode helpers ---


def handle_diag_opcode(op: Opcode) -> Opcode | None:
    """Return response opcode for diagnostic commands."""
    if op == Opcode.DIAG_PING:
        return Opcode.DIAG_STATS
    return None


# --- Context-vector TLV ---


@dataclass(frozen=True, slots=True)
class ContextTLV:
    """Simple TLV container."""

    t: int
    v: bytes

    @property
    def length(self) -> int:
        """Return length of the value field."""

        return len(self.v)

    def encode(self) -> bytes:
        return bytes([self.t, self.length]) + self.v


def decode_tlv(data: bytes) -> Tuple[ContextTLV, bytes]:
    t = data[0]
    length = data[1]
    v = data[2 : 2 + length]  # noqa: E203
    return ContextTLV(t, v), data[2 + length :]  # noqa: E203
