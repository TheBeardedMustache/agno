import pytest
from src.sqly import parse
from src.sqly.lowering import lower
from src.ntru import generate_keypair

pytest.importorskip("pytest_benchmark")

QUERY = " ".join(f"w{i}" for i in range(5000))
KEYPAIR = generate_keypair()
THRESHOLD = 0.12


@pytest.mark.benchmark(group="sqly")
def test_sqly_pipeline_benchmark(benchmark):
    def run():
        ast = parse(QUERY)
        lower(ast, "intent", KEYPAIR)

    benchmark(run)
    mean = getattr(benchmark.stats, "mean", None)
    if mean is None:
        mean = benchmark.stats.stats.mean
    assert mean < THRESHOLD
