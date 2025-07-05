from __future__ import annotations

"""Interactive SQLy REPL."""

from typing import Iterable
import argparse
import sys
import readline
from pathlib import Path

from . import parse, optimiser
from .lowering import lower
from ..ntru import generate_keypair
from ..sil.frame import Frame
from ..sil.diag import MirrorMode
from ..sil import config

PROMPT = "» "
HISTORY_FILE = Path.home() / ".sqly_history"


def _display_frames(frames: Iterable[Frame], mirror: MirrorMode) -> None:
    items = list(frames)
    print(f"Frames: {len(items)}")
    for frame in items:
        encoded_bytes = frame.encode().encode("ascii")
        hex_str = encoded_bytes.hex()
        print(hex_str[:128])
        preview = ""
        if frame.context_vector is not None:
            preview = frame.context_vector.v.decode("utf-8", "replace")
        print(f"{preview} | QoS={frame.qos} | Δt={frame.window}")
        mirror.record(hex_str)
    mirror.tick()
    if mirror.enabled:
        for payload in mirror.contents():
            print(f"mirror: {payload}")


def _process_query(text: str, mirror: MirrorMode) -> None:
    ast = parse(text)
    before = 1 + len(ast.phrases) + len(ast.signal_tags)
    opt_ast = optimiser.optimise(ast)
    after = 1 + len(opt_ast.phrases) + len(opt_ast.signal_tags)
    saved = before - after
    frames = lower(opt_ast, "query", generate_keypair(), do_optimise=False)
    print(f"Optimiser saved {saved} frame(s)")
    _display_frames(frames, mirror)


def main(argv: list[str] | None = None) -> None:  # pragma: no cover - CLI
    parser = argparse.ArgumentParser(prog="sqly", description="SQLy interactive REPL")
    parser.add_argument(
        "--stdin", action="store_true", help="read query from stdin and exit"
    )
    args = parser.parse_args(argv)

    mirror = MirrorMode()

    if args.stdin:
        text = sys.stdin.read()
        _process_query(text, mirror)
        return

    if HISTORY_FILE.exists():
        try:
            readline.read_history_file(HISTORY_FILE)
        except OSError:
            pass

    print(f"Energy budget: {config.ENERGY_BUDGET}")
    while True:
        try:
            text = input(PROMPT)
        except EOFError:
            break
        if not text:
            continue
        if text.startswith(":"):
            cmd = text.split()
            if cmd[0] == ":mirror" and len(cmd) == 2:
                if cmd[1] == "on":
                    mirror.enable()
                    print("mirror mode on")
                elif cmd[1] == "off":
                    mirror.disable()
                    print("mirror mode off")
                else:
                    print("usage: :mirror on|off")
            elif cmd[0] == ":budget" and len(cmd) == 2:
                val = cmd[1].upper()
                if val in {"LOW", "MED", "HIGH"}:
                    config.ENERGY_BUDGET = val
                    print(f"budget set to {val}")
                else:
                    print("usage: :budget <LOW|MED|HIGH>")
            elif cmd[0] in {":quit", ":exit"}:
                break
            else:
                print(f"unknown command: {cmd[0]}")
            continue
        try:
            _process_query(text, mirror)
        except Exception as exc:
            print(f"error: {exc}")

    try:
        readline.write_history_file(HISTORY_FILE)
    except OSError:
        pass


if __name__ == "__main__":  # pragma: no cover - manual entry
    main()
