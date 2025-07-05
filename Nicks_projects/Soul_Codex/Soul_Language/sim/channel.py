from __future__ import annotations

import random

from src.sil.frame import Frame


class LatencyChannel:
    """Simple latency channel applying Gaussian jitter."""

    def __init__(self, latency_us: float, jitter_us: float) -> None:
        self.latency_us = latency_us
        self.jitter_us = jitter_us

    def transmit(self, frame: Frame) -> float:  # noqa: ARG002
        """Return arrival time for ``frame`` in microseconds."""
        delay = random.gauss(self.latency_us, self.jitter_us)
        if delay < 0:
            delay = 0.0
        return delay
