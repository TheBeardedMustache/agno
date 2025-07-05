"""Lowering pass converting SQLy AST into SIL frames."""

from __future__ import annotations

from typing import List, Tuple

from .ast import Query

from ..sil.frame import Frame
from ..sil.opcode import Opcode
from ..sil.diag import ContextTLV
from . import optimiser

DEFAULT_MRI_PATH = "/tmp/mock_mri"
PHRASE_TAG = 2
SIGNAL_TAG = 3


def _make_context_frame(mri_path: str) -> Frame:
    tlv = ContextTLV(1, mri_path.encode("utf-8"))
    frame = Frame(
        ttt=0,
        window=0,
        qos=0,
        opcode=Opcode.NO_OP,
        context_vector=tlv,
    )
    return frame


def lower(
    ast: Query,
    intent_str: str,
    keypair: Tuple[bytes, bytes],
    *,
    do_optimise: bool = True,
) -> List[Frame]:
    """Lower ``ast`` into signed SIL :class:`Frame` objects."""

    if do_optimise:
        ast = optimiser.optimise(ast)

    pub, priv = keypair
    frames: List[Frame] = []

    # initial context vector frame
    context_frame = _make_context_frame(DEFAULT_MRI_PATH)
    context_frame.sign(priv, intent_str)
    frames.append(context_frame)

    # create a frame per phrase without signing to keep the lowering
    # pass lightweight; only the initial context frame is signed.
    for phrase in ast.phrases:
        tlv = ContextTLV(PHRASE_TAG, phrase.text.encode("utf-8"))
        frame = Frame(
            ttt=1,
            window=0,
            qos=0,
            opcode=Opcode.NO_OP,
            context_vector=tlv,
        )
        frames.append(frame)

    # create frames for signal tags
    for tag in ast.signal_tags:
        tlv = ContextTLV(SIGNAL_TAG, tag.encode("utf-8"))
        frame = Frame(
            ttt=2,
            window=0,
            qos=0,
            opcode=Opcode.NO_OP,
            context_vector=tlv,
        )
        frames.append(frame)

    return frames


__all__ = ["lower", "DEFAULT_MRI_PATH"]
