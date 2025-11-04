# src/bfs.py
from collections import deque
import time
import os
from maze_loader import load_map
from visualize import visualize_path

def bfs(grid, start, goal):
    """
    Breadth-First Search for shortest path in an unweighted grid.
    grid: 2D list of chars ('.' = open, '@'/'T' = blocked)
    start: (row, col)
    goal: (row, col)
    Returns: path list [(r,c), ...], number of explored nodes, runtime
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set([start])
    parent = {}

    start_time = time.time()

    while queue:
        r, c = queue.popleft()

        if (r, c) == goal:
            break

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] == "."
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

    runtime = time.time() - start_time

    # reconstruct path
    path = []
    node = goal
    while node in parent:
        path.append(node)
        node = parent[node]
    if path:
        path.append(start)
        path.reverse()

    return path, len(visited), runtime


def find_free_cell(grid, offset=0):
    """Find the first open '.' cell starting from a given offset."""
    for r in range(offset, len(grid)):
        for c in range(offset, len(grid[0])):
            if grid[r][c] == ".":
                return (r, c)
    return None


# quick test
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(base_dir, "../data/maps/brc100d.map")
    grid = load_map(map_path)

    start = find_free_cell(grid, offset=10)
    goal = find_free_cell(grid, offset=300)
    print(f"Start: {start}, Goal: {goal}")

    path, explored, runtime = bfs(grid, start, goal)
    print(
        f"BFS completed. Path length: {len(path)}, explored nodes: {explored}, runtime: {runtime:.3f}s"
    )

    # optional: print first few path points
    print("Path sample:", path[:10])

    visualize_path(grid, path, start, goal)