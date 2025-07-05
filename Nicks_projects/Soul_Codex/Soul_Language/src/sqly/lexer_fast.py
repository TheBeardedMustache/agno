from __future__ import annotations

try:
    import regex as re  # type: ignore
except Exception as exc:  # pragma: no cover - optional dependency
    raise ImportError("regex module not available") from exc

from typing import Iterator

from .token import Token, TokenPool
from .lexer import SqlyLexError

_TOKEN_RE = re.compile(
    r"(?P<SIGNAL_TAG>#[A-Za-z0-9-]+)"
    r"|(?P<GLYPH>[A-Za-z0-9]+)"
    r"|(?P<WS>\s+)"
    r"|(?P<INVALID>.)",
    re.ASCII,
)

_POOL = TokenPool()


def lex(text: str) -> Iterator[Token]:
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
        yield _POOL.acquire(kind, value)
    if pos != len(text):
        raise SqlyLexError(f"unable to match token at position {pos}")


def lex_tokens(text: str) -> list[Token]:
    return list(lex(text))
