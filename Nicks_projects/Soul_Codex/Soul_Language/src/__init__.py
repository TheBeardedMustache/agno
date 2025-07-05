"""Soul Language library."""

from hypothesis import settings

__version__ = "1.0.0"

settings.register_profile("codex", deadline=None)
settings.load_profile("codex")

from .frame import DeltaTQoS, TernaryTypedToken  # noqa: E402
from .extension7 import RLEText  # noqa: E402

__all__ = ["DeltaTQoS", "TernaryTypedToken", "RLEText", "__version__"]
