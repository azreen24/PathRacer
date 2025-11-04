# src/maze_loader.py
def load_map(file_path):
    """
    Reads a MovingAI.map file and returns a 2D grid.
    Each cell will be:
      '.' = free space
      '@' = obstacle
      'T' = tree (treat as obstacle)
    """
    grid = []
    reading_grid = False

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            # The map file starts after the line "map"
            if line.lower() == "map":
                reading_grid = True
                continue
            if reading_grid:
                grid.append(list(line))
    return grid


# Quick test
import os

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory of this script
    path = os.path.join(base_dir, "../data/maps/brc100d.map")

    print("Using path:", os.path.abspath(path))  # debug print
    maze = load_map(path)
    print(f"Loaded map with {len(maze)} rows and {len(maze[0])} columns")
    print("Sample row:", "".join(maze[0][:100]))