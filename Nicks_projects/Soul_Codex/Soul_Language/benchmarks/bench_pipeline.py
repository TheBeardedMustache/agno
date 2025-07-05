import cProfile
from pathlib import Path

from src.sqly import parse
from src.sqly.lowering import lower
from src.ntru import generate_keypair

CORPUS = Path(__file__).with_name("sample_corpus.txt").read_text()
KEYPAIR = generate_keypair()


def bench_pipeline(benchmark):
    def run():
        ast = parse(CORPUS)
        lower(ast, "intent", KEYPAIR)

    return benchmark(run)


if __name__ == "__main__":
    profile_path = Path(__file__).with_suffix(".prof")
    prof = cProfile.Profile()
    prof.runcall(lambda: lower(parse(CORPUS), "intent", KEYPAIR))
    prof.dump_stats(profile_path)
    import pstats

    stats = pstats.Stats(prof).sort_stats("cumulative")
    stats.print_stats(10)
