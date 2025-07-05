import logging
import pytest
from src.sil import logger, config
from src.sil.frame import Frame, FrameEnergyError, FrameVersionError
from src.sil.opcode import Opcode


def test_over_budget(monkeypatch):
    monkeypatch.setattr(config, "ENERGY_BUDGET", "MED")
    frame = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP, budget_rank=2)
    encoded = frame.encode()
    with pytest.raises(FrameEnergyError):
        Frame.decode(encoded)


def test_major_mismatch(monkeypatch):
    monkeypatch.setattr(config, "SIL_VERSION", (2, 1))
    frame = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP, major=1)
    encoded = frame.encode()
    with pytest.raises(FrameVersionError):
        Frame.decode(encoded)


def test_minor_forward(monkeypatch, caplog):
    monkeypatch.setattr(config, "SIL_VERSION", (2, 1))
    caplog.set_level(logging.WARNING, logger=logger.name)
    frame = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP, minor=2)
    encoded = frame.encode()
    decoded = Frame.decode(encoded)
    assert decoded.minor == 2
    assert any("minor version" in r.message for r in caplog.records)
