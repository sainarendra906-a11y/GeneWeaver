import random
import time

from src.alignment.cpu_engine import find_alignments


def run_cpu_benchmark():
    random.seed(42)

    bases = "ATCG"
    guide = "ATCGATCGATCGATCGATCG"

    target = "".join(
        random.choices(bases, k=100_000)
    )

    print("GeneWeaver CPU Alignment Benchmark")
    print("-" * 40)
    print("Target length:", len(target))
    print("Guide length:", len(guide))

    start = time.perf_counter()

    results = find_alignments(
        guide,
        target,
        max_mismatches=3
    )

    elapsed = time.perf_counter() - start

    throughput = len(target) / elapsed

    print("Execution time:", round(elapsed, 6), "seconds")
    print("Throughput:", round(throughput, 2), "bases/second")
    print("Alignments found:", len(results))


if __name__ == "__main__":
    run_cpu_benchmark()