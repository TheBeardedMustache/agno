from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Optional, TYPE_CHECKING

from hypothesis import strategies as st

import logging

from .config import ENERGY_BUDGET, SIL_VERSION
from ..ttt import decode_ttt_header, encode_ttt_header
from ..ntru import derive_public_key, sign as ntru_sign, verify as ntru_verify
from .ethics import FrameEthicsError, RiteOfForgiveness
from .opcode import Opcode, decode_opcode, encode_opcode
from .diag import ContextTLV, decode_tlv

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from ..hal.phy import PhotonPHYBackend


class FrameEnergyError(RuntimeError):
    """Raised when a frame exceeds the node's energy budget."""


class FrameVersionError(RuntimeError):
    """Raised when a frame has an incompatible version."""


def encode_mirror_mode(enabled: bool) -> str:
    """Encode mirror-mode flag into a single trit."""

    return "1" if enabled else "0"


def decode_mirror_mode(trit: str) -> bool:
    """Decode mirror-mode flag from a single trit."""

    if trit not in ("0", "1"):
        raise ValueError("mirror-mode flag must be one of '0' or '1'")
    return trit == "1"


@dataclass(frozen=True, slots=True)
class DeltaTQoS:
    """Δt window and QoS class encoded in two and one trits."""

    window: int
    qos: int

    def encode(self) -> str:
        return encode_delta_t_qos(self.window, self.qos)


def encode_delta_t_qos(window: int, qos: int) -> str:
    """Encode ``window`` and ``qos`` into a 3-trit string."""
    if not 0 <= window < 9:
        raise ValueError("window must be between 0 and 8 inclusive")
    if not 0 <= qos < 3:
        raise ValueError("QoS class must be between 0 and 2 inclusive")

    w = window
    digits = []
    for _ in range(2):
        w, rem = divmod(w, 3)
        digits.append(str(rem))
    return "".join(reversed(digits)) + str(qos)


def decode_delta_t_qos(trits: str) -> DeltaTQoS:
    """Decode a 3-trit string representing ``Δt`` window and QoS class."""
    if len(trits) != 3 or any(ch not in "012" for ch in trits):
        raise ValueError("Δt/QoS field must be three trits")
    window = int(trits[0]) * 3 + int(trits[1])
    qos = int(trits[2])
    return DeltaTQoS(window=window, qos=qos)


@dataclass(frozen=True, slots=True)
class EER:
    """Ethical Exception Register encoded as code + parity."""

    code: int
    parity: int

    def encode(self) -> str:
        return encode_eer(self.code, self.parity)


def encode_eer(code: int, parity: int) -> str:
    """Encode ``code`` and ``parity`` into a 6-trit string."""
    if not 0 <= code < 9:
        raise ValueError("EER code must be between 0 and 8 inclusive")
    if not 0 <= parity < 27:
        raise ValueError("EER parity must be between 0 and 26 inclusive")
    return encode_ttt_header(code) + encode_ttt_header(parity)


def decode_eer(trits: str) -> EER:
    """Decode a 6-trit string into :class:`EER`."""
    if len(trits) != 6 or any(ch not in "012" for ch in trits):
        raise ValueError("EER trailer must be six trits")
    code = decode_ttt_header(trits[:3]).value
    parity = decode_ttt_header(trits[3:]).value
    return EER(code=code, parity=parity)


def _encode_trits(value: int, width: int) -> str:
    """Return ``width`` trits encoding of ``value`` using digits 0, 1 and 2."""
    if not 0 <= value < 3**width:
        raise ValueError(f"value {value} does not fit in {width} trits")
    digits = []
    for _ in range(width):
        value, rem = divmod(value, 3)
        digits.append(str(rem))
    return "".join(reversed(digits))


def _intent_code_from_string(intent: str) -> str:
    digest = hashlib.sha3_256(intent.encode("utf-8")).digest()
    value = int.from_bytes(digest, "big") % (3**12)
    return _encode_trits(value, 12)


@dataclass(slots=True)
class SigLattice:
    """Signature block storing public key, intent code and signature."""

    public_key: bytes
    intent_code: str
    signature: bytes


@dataclass(frozen=True, slots=True)
class Frame:
    """Frame header with Δt/QoS, opcode and EER trailer."""

    ttt: int
    window: int
    qos: int
    opcode: Opcode
    budget_rank: int = 0
    major: int = SIL_VERSION[0]
    minor: int = SIL_VERSION[1]
    eer_code: int = 0
    eer_parity: int = 0
    sig_lattice: Optional[SigLattice] = None
    context_vector: Optional[ContextTLV] = None

    def encode(self) -> str:
        parts = [
            str(self.major),
            str(self.minor),
            str(self.budget_rank),
            encode_ttt_header(self.ttt),
            encode_delta_t_qos(self.window, self.qos),
            encode_opcode(self.opcode),
            encode_eer(self.eer_code, self.eer_parity),
        ]
        result = "".join(parts)
        if self.context_vector is not None:
            result += "|" + self.context_vector.encode().hex()
        return result

    @classmethod
    def decode(cls, trits: str) -> "Frame":
        tlv: Optional[ContextTLV] = None
        if "|" in trits:
            trits, tlv_hex = trits.split("|", 1)
            tlv_bytes = bytes.fromhex(tlv_hex)
            tlv, _ = decode_tlv(tlv_bytes)

        if len(trits) not in (12, 18) or any(ch not in "012" for ch in trits):
            raise ValueError("Frame must be twelve or eighteen trits")

        major = int(trits[0])
        minor = int(trits[1])
        budget = int(trits[2])

        ttt_val = decode_ttt_header(trits[3:6]).value
        delta = decode_delta_t_qos(trits[6:9])
        op = decode_opcode(trits[9:12])
        eer = EER(0, 0)
        if len(trits) == 18:
            eer = decode_eer(trits[12:])

        node_budget = {"LOW": 0, "MED": 1, "HIGH": 2, "MAX": 3}[ENERGY_BUDGET]
        if budget > node_budget:
            raise FrameEnergyError("energy budget exceeded")

        if major != SIL_VERSION[0]:
            raise FrameVersionError("major version mismatch")

        if minor > SIL_VERSION[1]:
            logger.warning("minor version %s ahead of node version", minor)

        return cls(
            ttt=ttt_val,
            window=delta.window,
            qos=delta.qos,
            opcode=op,
            budget_rank=budget,
            major=major,
            minor=minor,
            eer_code=eer.code,
            eer_parity=eer.parity,
            context_vector=tlv,
        )

    def validate(self) -> None:
        """Validate ethical status based on EER."""
        if self.eer_code != 0 or self.eer_parity != 0:
            RiteOfForgiveness.begin(self)
            raise FrameEthicsError("frame failed ethics validation")

    @staticmethod
    def intent_code(intent: str) -> str:
        """Return the 12-trit intent code for ``intent``."""
        return _intent_code_from_string(intent)

    def sign(self, private_key: bytes, intent: str) -> None:
        """Sign this frame using ``private_key`` and store signature block."""
        code = _intent_code_from_string(intent)
        message = self.encode().encode("ascii") + code.encode("ascii")
        signature = ntru_sign(private_key, message)
        pub = derive_public_key(private_key)
        object.__setattr__(
            self,
            "sig_lattice",
            SigLattice(public_key=pub, intent_code=code, signature=signature),
        )

    def verify(self, public_key: bytes) -> bool:
        """Verify frame signature using ``public_key``."""

        # fmt: off
        if (
            self.sig_lattice is None
            or self.sig_lattice.public_key != public_key
        ):
            return False
        message = (
            self.encode().encode("ascii")
            + self.sig_lattice.intent_code.encode("ascii")
        )
        # fmt: on
        return ntru_verify(public_key, message, self.sig_lattice.signature)

    def send(self, backend: "PhotonPHYBackend") -> None:
        """Send this frame via ``backend``."""
        backend.send(self.encode().encode("ascii"))

    def fuzz_verify(
        self,
        public_key: bytes,
        iterations: int = 1000,
        *,
        data: st.DataObject | None = None,
    ) -> int:
        """Mutate signature or intent code and count failed verifications."""

        if self.sig_lattice is None:
            raise ValueError("frame must be signed before fuzzing")

        import random
        from dataclasses import replace

        lattice = self.sig_lattice
        kills = 0

        for _ in range(iterations):
            mutate_sig = (
                data.draw(st.booleans())
                if data is not None
                else bool(random.getrandbits(1))
            )
            if mutate_sig:
                idx = (
                    data.draw(
                        st.integers(min_value=0, max_value=len(lattice.signature) - 1)
                    )
                    if data is not None
                    else random.randint(0, len(lattice.signature) - 1)
                )
                delta = (
                    data.draw(st.integers(min_value=1, max_value=255))
                    if data is not None
                    else random.randint(1, 255)
                )
                sig_bytes = bytearray(lattice.signature)
                sig_bytes[idx] ^= delta & 0xFF
                mutated_sig = bytes(sig_bytes)
                mutated_code = lattice.intent_code
            else:
                idx = (
                    data.draw(
                        st.integers(min_value=0, max_value=len(lattice.intent_code) - 1)
                    )
                    if data is not None
                    else random.randint(0, len(lattice.intent_code) - 1)
                )
                delta = (
                    data.draw(st.integers(min_value=1, max_value=2))
                    if data is not None
                    else random.randint(1, 2)
                )
                trits = list(lattice.intent_code)
                trits[idx] = str((int(trits[idx]) + delta) % 3)
                mutated_code = "".join(trits)
                mutated_sig = lattice.signature

            mutated = replace(self)
            object.__setattr__(
                mutated,
                "sig_lattice",
                SigLattice(lattice.public_key, mutated_code, mutated_sig),
            )
            try:
                if not mutated.verify(public_key):
                    kills += 1
            except Exception:
                kills += 1

        return kills

    def is_within_dt_window(self, arrival_time_us: float) -> bool:
        """Return True if arrival falls within this frame's Δt window."""

        bounds = [3 * 4**i for i in range(8)]
        if self.window >= len(bounds):
            return True

        lower = 0 if self.window == 0 else bounds[self.window - 1]
        upper = bounds[self.window]
        if self.window == 0:
            return bool(arrival_time_us <= upper)
        return bool(lower < arrival_time_us <= upper)


__all__ = [
    "encode_mirror_mode",
    "decode_mirror_mode",
    "DeltaTQoS",
    "encode_delta_t_qos",
    "decode_delta_t_qos",
    "EER",
    "encode_eer",
    "decode_eer",
    "FrameEnergyError",
    "FrameVersionError",
    "Frame",
    "SigLattice",
    "encode_ttt_header",
    "decode_ttt_header",
]
