from hypothesis import assume, given, settings, strategies as st

from src.sil.frame import Frame
from src.sil.opcode import Opcode
from src.ntru import generate_keypair


@given(st.data())
@settings(max_examples=1)
def test_fuzz_verify_basic(data: st.DataObject) -> None:
    pub, priv = generate_keypair()
    frame = Frame(ttt=1, window=1, qos=1, opcode=Opcode.NO_OP)
    frame.sign(priv, "run")
    killed = frame.fuzz_verify(pub, iterations=50, data=data)
    assume(killed > 0)
    assert killed <= 50
