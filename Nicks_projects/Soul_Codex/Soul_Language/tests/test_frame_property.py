import pytest
from hypothesis import HealthCheck, given, settings, strategies as st

from src.sil import config
from src.sil.frame import Frame, FrameEnergyError
from src.sil.opcode import Opcode


@given(
    ttt=st.integers(min_value=0, max_value=26),
    window=st.integers(min_value=0, max_value=8),
    qos=st.integers(min_value=0, max_value=2),
    budget=st.integers(min_value=0, max_value=2),
    eer_code=st.integers(min_value=0, max_value=8),
    eer_parity=st.integers(min_value=0, max_value=26),
)
@settings(max_examples=25, suppress_health_check=(HealthCheck.function_scoped_fixture,))
def test_decode_roundtrip(monkeypatch, ttt, window, qos, budget, eer_code, eer_parity):
    monkeypatch.setattr(config, "ENERGY_BUDGET", "MAX")
    monkeypatch.setattr("src.sil.frame.ENERGY_BUDGET", "MAX", raising=False)
    frame = Frame(
        ttt=ttt,
        window=window,
        qos=qos,
        opcode=Opcode.NO_OP,
        budget_rank=budget,
        eer_code=eer_code,
        eer_parity=eer_parity,
    )
    encoded = frame.encode()
    assert Frame.decode(encoded) == frame


@given(budget=st.integers(min_value=1, max_value=2))
@settings(max_examples=10, suppress_health_check=(HealthCheck.function_scoped_fixture,))
def test_decode_over_budget(monkeypatch, budget):
    monkeypatch.setattr(config, "ENERGY_BUDGET", "LOW")
    monkeypatch.setattr("src.sil.frame.ENERGY_BUDGET", "LOW", raising=False)
    frame = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP, budget_rank=budget)
    with pytest.raises(FrameEnergyError):
        Frame.decode(frame.encode())
