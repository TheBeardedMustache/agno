import random

import pytest

from sim.channel import LatencyChannel
from src.sil.frame import Frame
from src.sil.opcode import Opcode


@pytest.mark.parametrize(
    "window,qos,latency,expect",
    [
        (0, 0, 2.0, True),
        (0, 0, 4.0, False),
        (2, 1, 30.0, True),
        (2, 1, 10.0, False),
        (2, 1, 60.0, False),
        (8, 2, 10.0, True),
        (8, 2, 70.0, True),
    ],
)
def test_dt_window_qos(window, qos, latency, expect):
    random.seed(0)
    channel = LatencyChannel(latency_us=latency, jitter_us=0.5)
    frame = Frame(ttt=0, window=window, qos=qos, opcode=Opcode.NO_OP)
    arrival = channel.transmit(frame)
    assert frame.is_within_dt_window(arrival) is expect


def test_channel_negative_latency():
    channel = LatencyChannel(latency_us=-1.0, jitter_us=0.0)
    frame = Frame(ttt=0, window=8, qos=2, opcode=Opcode.NO_OP)
    assert channel.transmit(frame) == 0.0
