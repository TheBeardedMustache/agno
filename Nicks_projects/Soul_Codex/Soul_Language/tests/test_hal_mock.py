from sim.channel import LatencyChannel
from src.hal.phy import MockBackend
from src.sil.frame import Frame
from src.sil.opcode import Opcode


def test_mock_backend_loopback():
    backend = MockBackend(LatencyChannel(latency_us=0.0, jitter_us=0.0))
    frame = Frame(ttt=0, window=0, qos=0, opcode=Opcode.NO_OP)
    frame.send(backend)
    data = backend.recv(timeout_ms=1)
    assert data is not None
    decoded = Frame.decode(data.decode("ascii"))
    assert decoded == frame
