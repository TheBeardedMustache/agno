"""SQLy lexer implementation."""

from __future__ import annotations

try:
    import re2 as re  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    import re
from typing import Iterator

from .token import Token, TokenPool


class SqlyLexError(Exception):
    """Raised when lexing fails."""


_TOKEN_RE = re.compile(
    r"(?P<SIGNAL_TAG>#[A-Za-z0-9-]+)"  # signal tag like #tag
    r"|(?P<GLYPH>[A-Za-z0-9]+)"  # contiguous glyph characters
    r"|(?P<WS>\s+)"  # whitespace to skip
    r"|(?P<INVALID>.)",  # any other single character
    re.ASCII,
)

_TOKEN_POOL = TokenPool()


def lex(text: str) -> Iterator[Token]:
    """Lex ``text`` into a stream of :class:`Token` objects."""

    scanner = _TOKEN_RE.scanner(text)
    pos = 0
    for m in iter(scanner.match, None):
        if m.start() != pos:
            raise SqlyLexError(f"unable to match token at position {pos}")
        pos = m.end()
        kind = m.lastgroup
        value = m.group(kind)
        if kind == "WS":
            continue
        if kind == "INVALID":
            raise SqlyLexError(f"invalid token: {value}")
        yield _TOKEN_POOL.acquire(kind, value)
    if pos != len(text):
        raise SqlyLexError(f"unable to match token at position {pos}")


def lex_tokens(text: str) -> list[Token]:
    """Return a list of tokens for ``text``."""
    return list(lex(text))


__all__ = ["Token", "TokenPool", "SqlyLexError", "lex", "lex_tokens"]
