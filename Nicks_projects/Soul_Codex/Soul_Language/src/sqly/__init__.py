"""SQLy query language utilities."""

from .token import Token, TokenPool
from .lexer import SqlyLexError

try:  # pragma: no cover - optional dependency
    from .lexer_fast import lex, lex_tokens
except Exception:  # pragma: no cover - fallback
    from .lexer import lex, lex_tokens
from .parser import (
    SqlyParseError,
    Modifier,
    Phrase,
    Query,
    parse,
    parse_tokens,
    parse_fast,
    NodePool,
)
from .decoder import decode_frames
from .optimiser import optimise

__all__ = [
    "Token",
    "TokenPool",
    "SqlyLexError",
    "lex",
    "lex_tokens",
    "SqlyParseError",
    "Modifier",
    "Phrase",
    "Query",
    "parse",
    "parse_fast",
    "parse_tokens",
    "NodePool",
    "decode_frames",
    "optimise",
]
