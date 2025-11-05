"""
Benchmarks BFS and Dijkstra algorithms on selected maps.

For each map, both algorithms are executed multiple times to measure:
    • Average runtime (seconds)
    • Average number of explored nodes
    • Average path length

Results are printed to the console in a formatted table for comparison.
"""

import os
import statistics
from maze_loader import load_map
from bfs import bfs
from dijkstra import dijkstra


def benchmark_algorithms():
    """
    Run performance benchmarks for BFS and Dijkstra.

    The function loops over each map and algorithm, running each
    several times to obtain stable average metrics.

    Returns:
        list of tuples (map_name, algorithm, avg_time, avg_explored, avg_path)
    """

    # configuration 
    base = os.path.dirname(os.path.abspath(__file__))   
    maps = ["DragonsAgeOrigins", "BauldersGateII"]      
    num_runs = 5                                       

    results = []  

    print("=== PathFinder Benchmark ===")
    print(f"Running {num_runs} trials per algorithm per map...\n")

    # main benchmark loop 
    for map_name in maps:
        # locate and load map file
        map_path = os.path.join(base, f"../data/maps/{map_name}.map")
        grid = load_map(map_path)

        # consistent start/goal used across tests
        start = (131, 297)
        goal = (300, 300)

        # loop through both algorithms
        for alg_name, alg_func in [("BFS", bfs), ("Dijkstra", dijkstra)]:
            runtimes, explored_counts, path_lengths = [], [], []

            # run each algorithm multiple times for stable averages
            for _ in range(num_runs):
                path, explored, runtime = alg_func(grid, start, goal)
                runtimes.append(runtime)
                explored_counts.append(explored)
                path_lengths.append(len(path))

            # compute averages
            avg_time = statistics.mean(runtimes)
            avg_explored = statistics.mean(explored_counts)
            avg_path = statistics.mean(path_lengths)

            # save results
            results.append((map_name, alg_name, avg_time, avg_explored, avg_path))

            # formatted console output
            print(f"{map_name:<18} | {alg_name:<9} | "
                  f"Avg time: {avg_time:.4f}s | "
                  f"Explored: {avg_explored:>7.0f} | "
                  f"Path length: {avg_path:.0f}")

    return results


# entry point
if __name__ == "__main__":
    benchmark_algorithms()
