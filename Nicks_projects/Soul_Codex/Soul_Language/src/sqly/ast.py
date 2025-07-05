from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class Modifier:
    value: str

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.value


@dataclass(slots=True)
class Phrase:
    text: str
    modifiers: List[Modifier] = field(default_factory=list)
    merged: bool = False

    def __str__(self) -> str:  # pragma: no cover - trivial
        mods = "".join(str(m) for m in self.modifiers)
        return f"{mods}{self.text}"


@dataclass(slots=True)
class Query:
    phrases: List[Phrase] = field(default_factory=list)
    signal_tags: List[str] = field(default_factory=list)

    def __str__(self) -> str:  # pragma: no cover - trivial
        parts = [str(p) for p in self.phrases]
        parts.extend(self.signal_tags)
        return " ".join(parts)


class NodePool:
    __slots__ = ["_phrases", "_mods"]

    def __init__(self) -> None:
        self._phrases: list[Phrase] = []
        self._mods: list[Modifier] = []

    def acquire_phrase(self, text: str) -> Phrase:
        try:
            node = self._phrases.pop()
            node.text = text
            node.modifiers.clear()
            node.merged = False
            return node
        except IndexError:
            return Phrase(text)

    def release_phrase(self, phrase: Phrase) -> None:
        self._phrases.append(phrase)

    def acquire_modifier(self, value: str) -> Modifier:
        try:
            node = self._mods.pop()
            node.value = value
            return node
        except IndexError:
            return Modifier(value)

    def release_modifier(self, mod: Modifier) -> None:
        self._mods.append(mod)
