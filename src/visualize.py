import matplotlib.pyplot as plt
import numpy as np

def visualize_path(grid, path, start, goal, save_path="../results/bfs_path.png"):
    rows, cols = len(grid), len(grid[0])
    maze_array = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ("@", "T"):
                maze_array[r, c] = 1

    plt.figure(figsize=(8, 8))
    plt.imshow(maze_array, cmap="gray_r", origin="upper")

    if path:
        pr, pc = zip(*path)
        plt.plot(pc, pr, color="red", linewidth=1.2, label="Shortest Path")

    plt.scatter(start[1], start[0], color="green", marker="o", s=30, label="Start")
    plt.scatter(goal[1], goal[0], color="blue", marker="x", s=30, label="Goal")
    plt.title("BFS Path Visualization")
    plt.legend()
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150)
    plt.close()

    print(f"Saved visualization to {save_path}")
