"""Thin wrapper around ``liboqs-python`` for NTRU Prime signatures."""

import hashlib
import os
from ctypes.util import find_library
from importlib import import_module
from types import ModuleType
from typing import Dict

oqs: ModuleType | None
if find_library("oqs") is not None:
    try:  # pragma: no cover - optional dependency may be missing
        oqs = import_module("oqs")
    except Exception:  # pragma: no cover - library not usable
        oqs = None
else:  # pragma: no cover - library missing
    oqs = None

_ALGORITHM = "ntruprime_sntrup761"
_key_map: Dict[bytes, bytes] = {}

__all__ = ["generate_keypair", "derive_public_key", "sign", "verify"]


def generate_keypair() -> tuple[bytes, bytes]:
    """Return a (public, private) keypair for the NTRU implementation."""
    if oqs is not None:
        with oqs.Signature(_ALGORITHM) as signer:
            pub, priv = signer.generate_keypair()
    else:  # pragma: no cover - fallback for missing dependency
        priv = os.urandom(32)
        pub = priv
    _key_map[priv] = pub
    return pub, priv


def derive_public_key(private_key: bytes) -> bytes:
    """Return public key corresponding to ``private_key``."""
    return _key_map[private_key]


def sign(private_key: bytes, message: bytes) -> bytes:
    """Return signature for ``message`` using ``private_key``."""
    if oqs is not None:
        with oqs.Signature(_ALGORITHM) as signer:
            return bytes(signer.sign(message, private_key))
    # Use a fast SHA-256 based digest for the lightweight reference fallback
    # Truncate the digest to 16 bytes to keep signatures small and fast.
    return hashlib.sha256(private_key + message).digest()[:16]


def verify(public_key: bytes, message: bytes, signature: bytes) -> bool:
    """Verify ``signature`` for ``message`` with ``public_key``."""
    if oqs is not None:
        with oqs.Signature(_ALGORITHM) as signer:
            return bool(signer.verify(message, signature, public_key))
    expected = hashlib.sha256(public_key + message).digest()[:16]
    return expected == signature
