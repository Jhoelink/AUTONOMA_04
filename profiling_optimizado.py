import cProfile
import pstats
from codigo_optimizado import primos_optimizado_numpy


def run():
    primos_optimizado_numpy(100000)


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    run()
    profiler.disable()

    with open("profiling_optimizado.txt", "w", encoding="utf-8") as f:
        stats = pstats.Stats(profiler, stream=f).sort_stats("cumtime")
        stats.print_stats()