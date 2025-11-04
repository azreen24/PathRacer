import heapq
import os
import time
from maze_loader import load_map
from visualize import visualize_path


def dijkstra(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = {start: 0}
    parent = {start: None}
    visited = set()
    pq = [(0, start)]
    explored = 0
    start_time = time.time()

    while pq:
        dist, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        explored += 1

        if current == goal:
            break

        for dr, dc in moves:
            nr, nc = current[0] + dr, current[1] + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in ("@", "T"):
                new_dist = dist + 1
                if new_dist < distances.get((nr, nc), float("inf")):
                    distances[(nr, nc)] = new_dist
                    parent[(nr, nc)] = current
                    heapq.heappush(pq, (new_dist, (nr, nc)))

    runtime = time.time() - start_time

    # Path reconstruction
    path = []
    node = goal
    if node not in parent:
        print("Goal not reached.")
        return [], explored, runtime
    while node:
        path.append(node)
        node = parent[node]
    path.reverse()

    return path, explored, runtime


def find_free_cell(grid, offset=0):
    """Find the first open '.' cell starting from a given offset."""
    for r in range(offset, len(grid)):
        for c in range(offset, len(grid[0])):
            if grid[r][c] == ".":
                return (r, c)
    return None


# --- Quick test ---
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    map_path = os.path.join(base_dir, "../data/maps/brc100d.map")
    grid = load_map(map_path)

    # use same dynamic start/goal logic as BFS
    start = find_free_cell(grid, offset=10)
    goal = find_free_cell(grid, offset=300)

    print("Start:", start, "=", grid[start[0]][start[1]])
    print("Goal:", goal, "=", grid[goal[0]][goal[1]])

    print("Running Dijkstra’s Algorithm...")
    path, explored, runtime = dijkstra(grid, start, goal)
    print(f"Path length: {len(path)}, explored nodes: {explored}, runtime: {runtime:.3f}s")

    visualize_path(grid, path, start, goal,
               save_path="../results/dijkstra_path.png",
               title="Dijkstra Path Visualization")