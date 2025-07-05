from src.sqly.parser import parse
from src.sqly.lowering import lower, DEFAULT_MRI_PATH
from src.ntru import generate_keypair


def test_lowering_signature_and_context():
    ast = parse("foo bar #sig")
    pub, priv = generate_keypair()
    frames = lower(ast, "query", (pub, priv))
    assert frames

    first = frames[0]
    assert first.verify(pub)
    assert first.context_vector.v.decode() == DEFAULT_MRI_PATH
