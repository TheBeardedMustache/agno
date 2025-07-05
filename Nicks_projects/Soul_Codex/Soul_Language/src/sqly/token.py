from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Token:
    """Single lexical token."""

    type: str
    value: str


class TokenPool:
    """Simple object pool for :class:`Token` instances."""

    __slots__ = ["_pool"]

    def __init__(self) -> None:
        self._pool: list[Token] = []

    def acquire(self, token_type: str, value: str) -> Token:
        try:
            tok = self._pool.pop()
            tok.type = token_type
            tok.value = value
            return tok
        except IndexError:
            return Token(token_type, value)

    def release(self, token: Token) -> None:
        self._pool.append(token)
