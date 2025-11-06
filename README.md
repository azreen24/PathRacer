# PathFinder: BFS vs Dijkstra Maze Visualization and Analysis

Author: Azreen Haque  
Course: COP3530 – Data Structures and Algorithms  
University of Florida

## Overview

PathFinder is a Python-based visualization and benchmarking tool that compares two classic shortest path algorithms—Breadth-First Search (BFS) and Dijkstra’s Algorithm—on real map data from the MovingAI Pathfinding Benchmark Dataset.

The project demonstrates each algorithm’s behavior and efficiency through an interactive Tkinter GUI, with embedded Matplotlib visualizations and performance metrics such as runtime, nodes explored, and path length.

## Objectives

- Implement and compare BFS and Dijkstra on 2D grid maps  
- Provide an interactive GUI for algorithm and map selection  
- Visualize shortest paths and traversal statistics in real time  
- Benchmark algorithm performance across multiple maps  
- Analyze complexity and runtime differences in practice

## Features

- BFS and Dijkstra implementations for grid-based maps  
- Tkinter GUI with dropdown selectors for algorithm and map  
- Matplotlib visualizations of the shortest path  
- Benchmarking module to calculate average runtime and nodes explored  
- Automatic detection of valid start and goal cells  
- Support for custom `.map` files in MovingAI format

## Project Structure

```
PathRacer/
│
├── src/
│   ├── bfs.py                 # BFS implementation
│   ├── dijkstra.py            # Dijkstra implementation
│   ├── maze_loader.py         # Loads MovingAI map files
│   ├── visualize.py           # Handles Matplotlib visualization
│   ├── main_ui.py             # Tkinter GUI controller
│   ├── benchmark.py           # Benchmarking tool
│   └── test_algorithms.py     # Verifies correctness between BFS and Dijkstra
│
├── data/
│   └── maps/
│       ├── DragonsAgeOrigins.map
│       ├── BauldersGateII.map
│       └── (add more .map files here)
│
├── results/
│   └── (generated visualization images, optional)
│
└── README.md
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/azreen24/PathRacer.git
   cd PathRacer/src
   ```

2. Install dependencies:
   ```bash
   pip install matplotlib numpy
   ```
   Tkinter is included with most Python installations.

## Usage

### Run the GUI
```bash
python main_ui.py
```
The interface allows selection of BFS or Dijkstra and a map file.  
Click “Run Algorithm” to execute and visualize results.

### Run Benchmarks
```bash
python benchmark.py
```
This script runs both algorithms multiple times per map and prints:
- Average runtime (seconds)
- Nodes explored
- Path length

### Test Algorithm Correctness
```bash
python test_algorithms.py
```
Verifies that BFS and Dijkstra produce identical path lengths in unweighted maps.

## Algorithms Implemented

### Breadth-First Search (BFS)
Guarantees the shortest path in unweighted grids.  
Uses a queue to explore nodes level by level.  
Time Complexity: O(V + E)  
Space Complexity: O(V)

### Dijkstra’s Algorithm
General shortest path algorithm using a priority queue.  
Produces the same result as BFS for unweighted grids but with higher overhead.  
Time Complexity: O((V + E) log V)  
Space Complexity: O(V)

## Example Benchmark Results

| Map               | Algorithm | Avg Time (s) | Nodes Explored | Path Length |
|-------------------|------------|--------------|----------------|--------------|
| DragonsAgeOrigins | BFS        | 0.012        | 10061          | 247          |
| DragonsAgeOrigins | Dijkstra   | 0.020        | 10056          | 247          |
| BauldersGateII    | BFS        | 0.034        | 15000          | 369          |
| BauldersGateII    | Dijkstra   | 0.056        | 15000          | 369          |

BFS is faster for unweighted maps because it uses constant-time queue operations, while Dijkstra incurs heap overhead.

## Design Choices

- Implemented in Python for rapid development and better visualization support  
- Focused on core features—correctness, GUI integration, and performance analysis  
- Converted from original C++ group proposal to a solo Python project for efficiency and manageability

## Reflection

Developing PathFinder independently required combining algorithm design, GUI programming, and visualization.  
The project strengthened understanding of BFS and Dijkstra and made their theoretical differences tangible.  
Challenges included embedding Matplotlib inside Tkinter and tuning layout for different maps.  
Overall, it provided valuable experience integrating data structures, algorithms, and user interfaces.

## References

- MovingAI Pathfinding Benchmarks Dataset – https://movingai.com/benchmarks/grids.html  
- Python Documentation – `heapq`, `matplotlib`, `tkinter`  
- COP3530 Lecture Notes – Graph Traversal and Search Algorithms, University of Florida

## Future Work

- Implement A* Search for heuristic comparison  
- Add weighted map support  
- Create animated path exploration  
- Export benchmark results to CSV and visualize with plots

## Author

Azreen Haque  
University of Florida  
GitHub: https://github.com/azreen24
