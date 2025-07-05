from __future__ import annotations

from typing import Iterable, List

from .ast import Phrase, Query
from ..sil.frame import Frame


def decode_frames(frames: Iterable[Frame]) -> Query:
    """Reconstruct a ``Query`` from a sequence of ``Frame`` objects."""

    phrases: List[Phrase] = []
    signal_tags: List[str] = []
    for frame in frames:
        if frame.ttt == 0:
            # context frame, ignore its TLV for the query itself
            continue
        tlv = frame.context_vector
        if tlv is None:
            continue
        text = tlv.v.decode("utf-8")
        if frame.ttt == 1:
            phrases.append(Phrase(text))
        elif frame.ttt == 2:
            signal_tags.append(text)
    return Query(phrases, signal_tags)


__all__ = ["decode_frames"]
