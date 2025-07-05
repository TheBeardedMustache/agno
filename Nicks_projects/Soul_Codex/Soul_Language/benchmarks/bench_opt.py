from pathlib import Path

from src.sqly import parse
from src.sqly.lowering import lower
from src.ntru import generate_keypair

CORPUS = Path(__file__).with_name("bench_corpus.txt").read_text()
KEYPAIR = generate_keypair()


def bench_optimizer(benchmark):
    ast = parse(CORPUS)
    frames_before = len(ast.phrases) + len(ast.signal_tags) + 1

    def run():
        lower(ast, "intent", KEYPAIR)

    frames_after = len(lower(ast, "intent", KEYPAIR))
    reduction_percent = (frames_before - frames_after) / frames_before * 100

    assert reduction_percent >= 25

    benchmark(run)

    return frames_before, frames_after, reduction_percent


if __name__ == "__main__":
    fb, fa, r = bench_optimizer(lambda f: f())
    print(f"before={fb} after={fa} reduction={r:.2f}%")
