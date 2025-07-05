from hypothesis import HealthCheck, given, settings, strategies as st

from src.sil.frame import Frame
from src.sil.opcode import Opcode
from src.ntru import generate_keypair


@given(st.data())
@settings(max_examples=1, suppress_health_check=(HealthCheck.too_slow,))
def test_sig_fuzz_kill_rate(data: st.DataObject) -> None:
    pub, priv = generate_keypair()
    frame = Frame(ttt=1, window=1, qos=1, opcode=Opcode.NO_OP)
    frame.sign(priv, "run")
    assert frame.verify(pub)
    killed = frame.fuzz_verify(pub, iterations=1000, data=data)
    assert killed >= 990
