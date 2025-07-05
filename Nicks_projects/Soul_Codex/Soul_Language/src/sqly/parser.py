"""SQLy parser implementation."""

from __future__ import annotations

from typing import Iterable, List, Callable, Iterator, Optional

from .ast import (
    Modifier as ASTModifier,
    Phrase as ASTPhrase,
    Query as ASTQuery,
    NodePool,
)

from .lexer import Token, lex as slow_lex

fast_lex: Optional[Callable[[str], Iterator[Token]]]
try:  # pragma: no cover - optional dependency
    from .lexer_fast import lex as fast_lex
except Exception:  # pragma: no cover - optional dependency
    fast_lex = None


class SqlyParseError(Exception):
    """Raised when parsing fails."""


Modifier = ASTModifier
Phrase = ASTPhrase
Query = ASTQuery


def parse_tokens(tokens: Iterable[Token], pool: NodePool | None = None) -> Query:
    """Parse an iterable of :class:`Token` objects into a :class:`Query`."""

    phrases: List[Phrase] = []
    signal_tags: List[str] = []
    for tok in tokens:
        if tok.type == "GLYPH":
            if pool is not None:
                phrases.append(pool.acquire_phrase(tok.value))
            else:
                phrases.append(Phrase(tok.value))
        elif tok.type == "SIGNAL_TAG":
            signal_tags.append(tok.value)
        else:
            raise SqlyParseError(f"unexpected token type: {tok.type}")
    return Query(phrases, signal_tags)


def parse(text: str, *, pool: NodePool | None = None) -> Query:
    """Parse ``text`` into a :class:`Query`."""

    lexer = fast_lex if fast_lex is not None else slow_lex
    return parse_tokens(lexer(text), pool=pool)


def parse_fast(text: str, *, pool: NodePool | None = None) -> Query:
    """Parse using the accelerated lexer if available."""

    if fast_lex is None:
        return parse(text, pool=pool)
    return parse_tokens(fast_lex(text), pool=pool)


__all__ = [
    "SqlyParseError",
    "Modifier",
    "Phrase",
    "Query",
    "parse",
    "parse_tokens",
    "parse_fast",
    "NodePool",
]
