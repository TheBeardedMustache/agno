from __future__ import annotations

import time
from pathlib import Path

from src.sqly.lexer import lex as slow_lex
from src.sqly.parser import parse_fast, parse_tokens, NodePool
from src.sqly.lowering import lower
from src.ntru import generate_keypair

CORPUS = Path(__file__).with_name("bench_corpus.txt").read_text()
KEYPAIR = generate_keypair()
THRESHOLD = 0.20


def test_latency_speedup():
    pool = NodePool()
    start = time.perf_counter()
    ast = parse_tokens(slow_lex(CORPUS), pool)
    lower(ast, "intent", KEYPAIR)
    slow = time.perf_counter() - start

    start = time.perf_counter()
    ast = parse_fast(CORPUS, pool=pool)
    lower(ast, "intent", KEYPAIR)
    fast = time.perf_counter() - start

    assert (slow - fast) / slow >= THRESHOLD


if __name__ == "__main__":
    test_latency_speedup()
