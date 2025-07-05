from src.sqly.lexer import lex_tokens
from src.sqly.parser import parse_tokens


def test_parse_roundtrip():
    query = "foo bar baz #sig1 #sig2"
    tokens = lex_tokens(query)
    ast = parse_tokens(tokens)
    # Ensure phrases parsed correctly
    assert [p.text for p in ast.phrases] == ["foo", "bar", "baz"]
    # Signal tags stored separately
    assert ast.signal_tags == ["#sig1", "#sig2"]
    # Converting AST back to string should match original
    assert str(ast) == query
