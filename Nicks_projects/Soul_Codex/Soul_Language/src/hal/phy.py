from __future__ import annotations

from collections import deque
from typing import Deque, Optional

from sim.channel import LatencyChannel


class PhotonPHYBackend:
    """Abstract photon physical layer backend."""

    def send(self, frame_bytes: bytes) -> None:
        """Transmit ``frame_bytes`` over the physical layer."""
        raise NotImplementedError

    def recv(self, timeout_ms: int) -> Optional[bytes]:
        """Return received frame bytes or ``None`` if timed out."""
        raise NotImplementedError


class MockBackend(PhotonPHYBackend):
    """In-memory backend using :class:`LatencyChannel`."""

    def __init__(self, channel: Optional[LatencyChannel] = None) -> None:
        self.channel = channel or LatencyChannel(latency_us=0.0, jitter_us=0.0)
        self._queue: Deque[tuple[bytes, float]] = deque()

    def send(self, frame_bytes: bytes) -> None:
        from src.sil.frame import Frame

        frame = Frame.decode(frame_bytes.decode("ascii"))
        arrival = self.channel.transmit(frame)
        self._queue.append((frame_bytes, arrival))

    def recv(self, timeout_ms: int) -> Optional[bytes]:
        if not self._queue:
            return None
        frame_bytes, arrival = self._queue[0]
        if arrival <= timeout_ms * 1000:
            self._queue.popleft()
            return frame_bytes
        return None
