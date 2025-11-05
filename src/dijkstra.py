"""
Implements Dijkstra’s shortest path algorithm for grid-based maps.

The algorithm finds the minimum-cost path between a start and goal
position on a 2D map, where movement is allowed up, down, left, and right.

This version uses a min-heap priority queue for efficient selection of
the next closest node. Obstacles '@' and 'T' are treated as blocked cells.
"""

import heapq
import os
import time
from maze_loader import load_map
from visualize import visualize_path


def dijkstra(grid, start, goal):
    """
    Compute the shortest path using Dijkstra’s Algorithm.

    Args:
        grid (list[list[str]]): 2D map grid loaded from a .map file.
        start (tuple): Starting coordinates (row, col).
        goal (tuple): Goal coordinates (row, col).

    Returns:
        path (list[tuple]): Sequence of (row, col) cells forming the shortest path.
        explored (int): Number of nodes visited during search.
        runtime (float): Total execution time in seconds.
    """

    rows, cols = len(grid), len(grid[0])

    # Possible moves: up, down, left, right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Distance to each node (initialized to infinity except start)
    distances = {start: 0}

    # Parent dictionary for path reconstruction
    parent = {start: None}

    # Track visited nodes to prevent reprocessing
    visited = set()

    # Priority queue stores (distance, (row, col))
    pq = [(0, start)]

    explored = 0
    start_time = time.time()

    # Main search loop
    while pq:
        dist, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        explored += 1

        # Stop once the goal is reached
        if current == goal:
            break

        # Explore neighbors
        for dr, dc in moves:
            nr, nc = current[0] + dr, current[1] + dc

            # Skip cells outside the grid or blocked cells
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in ("@", "T"):
                new_dist = dist + 1  # uniform movement cost

                # Update distance if a shorter path is found
                if new_dist < distances.get((nr, nc), float("inf")):
                    distances[(nr, nc)] = new_dist
                    parent[(nr, nc)] = current
                    heapq.heappush(pq, (new_dist, (nr, nc)))

    runtime = time.time() - start_time

    # Path reconstruction
    path = []
    node = goal

    # If goal was never reached, return empty path
    if node not in parent:
        print("Goal not reached.")
        return [], explored, runtime

    # Backtrack from goal to start
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, explored, runtime


def find_free_cell(grid, offset=0):
    """
    Find the first open '.' cell in the grid starting from a given offset.

    Args:
        grid (list[list[str]]): Map grid.
        offset (int): Starting index for the search.

    Returns:
        tuple or None: Coordinates of first open cell or None if not found.
    """
    for r in range(offset, len(grid)):
        for c in range(offset, len(grid[0])):
            if grid[r][c] == ".":
                return (r, c)
    return None


if __name__ == "__main__":
    # Quick test: Run Dijkstra on a sample map and save visualization

    base_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(base_dir, "../data/maps/DragonsAgeOrigins.map")
    grid = load_map(map_path)

    # Dynamic selection of valid start and goal cells
    start = find_free_cell(grid, offset=10)
    goal = find_free_cell(grid, offset=300)

    print("Start:", start, "=", grid[start[0]][start[1]])
    print("Goal:", goal, "=", grid[goal[0]][goal[1]])

    print("Running Dijkstra’s Algorithm...")
    path, explored, runtime = dijkstra(grid, start, goal)
    print(f"Path length: {len(path)}, explored nodes: {explored}, runtime: {runtime:.3f}s")

    visualize_path(
        grid, path, start, goal,
        save_path="../results/dijkstra_path.png",
        title="Dijkstra Path Visualization"
    )