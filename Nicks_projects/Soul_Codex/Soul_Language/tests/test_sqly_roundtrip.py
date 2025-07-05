from src.sqly import parse
from src.sqly.lowering import lower
from src.sqly.decoder import decode_frames
from src.ntru import generate_keypair
from src.sil.frame import Frame


def test_sqly_roundtrip():
    query = "foo bar #sig"
    ast = parse(query)
    frames = lower(ast, "intent", generate_keypair())
    encoded = [f.encode() for f in frames]
    decoded = [Frame.decode(t) for t in encoded]
    decoded_ast = decode_frames(decoded)
    assert str(decoded_ast) == str(ast)
