from __future__ import annotations

import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - used for type hints only
    from .frame import Frame

log = logging.getLogger(__name__)


class FrameEthicsError(RuntimeError):
    """Raised when a frame fails ethics validation."""


class RiteOfForgiveness:
    """Utility class to initiate forgiveness procedures."""

    @staticmethod
    def begin(frame: "Frame") -> None:
        """Log violation context before further handling."""
        log.warning("Ethical violation detected: %r", frame)


__all__ = ["FrameEthicsError", "RiteOfForgiveness"]
