import pytest

from src.extension7 import encode_rle, decode_rle


@pytest.mark.parametrize(
    "text",
    [
        "abc",
        "aaabb",
        "a2b3",  # digits in original text
        "1111",
    ],
)
def test_roundtrip(text):
    encoded = encode_rle(text)
    decoded = decode_rle(encoded).text
    assert decoded == text


def test_specific_encoding():
    assert encode_rle("aa") == "a#2"
    assert encode_rle("a") == "a"
    assert encode_rle("a11") == "a1#2"
    assert decode_rle("a#3").text == "aaa"
