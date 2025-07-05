"""Query optimiser for SQLy."""

from __future__ import annotations

from dataclasses import replace
from typing import List

from .ast import Query, Phrase


def optimise(ast: Query) -> Query:
    """Merge consecutive phrases with identical context metadata."""

    if not ast.phrases:
        return ast

    new_phrases: List[Phrase] = []
    current = ast.phrases[0]
    key_text = current.text
    merged = False

    for phrase in ast.phrases[1:]:
        if phrase.text == key_text:
            current = replace(current, text=f"{current.text} {phrase.text}")
            merged = True
        else:
            if merged:
                current = replace(current, merged=True)
            new_phrases.append(current)
            current = phrase
            key_text = phrase.text
            merged = False

    if merged:
        current = replace(current, merged=True)
    new_phrases.append(current)

    return Query(new_phrases, list(ast.signal_tags))


__all__ = ["optimise"]
