import pytest

from src.sqly.lexer import Token, SqlyLexError, lex_tokens


def test_valid_query():
    query = "foo bar baz #sig1 #sig2"
    tokens = lex_tokens(query)
    assert tokens == [
        Token("GLYPH", "foo"),
        Token("GLYPH", "bar"),
        Token("GLYPH", "baz"),
        Token("SIGNAL_TAG", "#sig1"),
        Token("SIGNAL_TAG", "#sig2"),
    ]


def test_invalid_token():
    with pytest.raises(SqlyLexError):
        list(lex_tokens("foo$"))
