import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import statistics
import os

from maze_loader import load_map
from bfs import bfs
from dijkstra import dijkstra


# --- Style setup ---
BG_COLOR = "#1e1e1e"
PANEL_COLOR = "#2b2b2b"
TEXT_COLOR = "#ffffff"
ACCENT = "#ff5252"
FONT = ("Segoe UI", 11)
TITLE_FONT = ("Segoe UI Semibold", 20)


def draw_visualization(frame, grid, path, start, goal, title):
    for widget in frame.winfo_children():
        widget.destroy()

    rows, cols = len(grid), len(grid[0])
    maze_array = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ("@", "T"):
                maze_array[r, c] = 1

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(maze_array, cmap="gray_r", origin="upper")

    if path:
        pr, pc = zip(*path)
        ax.plot(pc, pr, color=ACCENT, linewidth=1.6, label="Shortest Path")

    ax.scatter(start[1], start[0], color="#00ff88", marker="o", s=35, label="Start")
    ax.scatter(goal[1], goal[0], color="#00b7ff", marker="x", s=35, label="Goal")
    ax.set_title(title, color=TEXT_COLOR, fontsize=13)
    ax.axis("off")
    ax.legend(facecolor="white")

    fig.patch.set_facecolor(BG_COLOR)
    ax.set_facecolor(BG_COLOR)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    plt.close(fig)


def run_algorithm(alg_choice, map_choice, frame, info_frame):
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        map_path = os.path.join(base, f"../data/maps/{map_choice}.map")
        grid = load_map(map_path)

        start = (131, 297)
        goal = (300, 300)

        num_runs = 5
        times = []
        path, explored = None, None

        if alg_choice == "BFS":
            for _ in range(num_runs):
                path, explored, runtime = bfs(grid, start, goal)
                times.append(runtime)
        else:
            for _ in range(num_runs):
                path, explored, runtime = dijkstra(grid, start, goal)
                times.append(runtime)

        runtime = statistics.mean(times)
        draw_visualization(frame, grid, path, start, goal, f"{alg_choice} on {map_choice}")

        for widget in info_frame.winfo_children():
            widget.destroy()

        # neatly formatted info box
        info_title = tk.Label(
            info_frame,
            text="Run Summary",
            font=("Segoe UI Semibold", 14),
            fg=ACCENT,
            bg=PANEL_COLOR,
            pady=5
        )
        info_title.pack()

        stats = (
            f"Algorithm: {alg_choice}\n"
            f"Map: {map_choice}\n"
            f"Path length: {len(path)}\n"
            f"Nodes explored: {explored}\n"
            f"Average runtime (5 runs): {runtime:.3f}s"
        )

        info_box = tk.Label(
            info_frame,
            text=stats,
            justify="left",
            font=("Consolas", 12),
            bg=PANEL_COLOR,
            fg="#e5e5e5",
            padx=10,
            pady=8,
            anchor="w"
        )
        info_box.pack(fill="both", expand=True)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI setup 
root = tk.Tk()
root.title("PathFinder Visual Interface")
root.configure(bg=BG_COLOR)
root.geometry("900x1000")

# Title
title_label = tk.Label(
    root, text="🧭 MazeRunners: PathFinder",
    font=TITLE_FONT, fg=ACCENT, bg=BG_COLOR, pady=15
)
title_label.pack()

# Control panel
control_frame = tk.Frame(root, bg=PANEL_COLOR, bd=2, relief="ridge")
control_frame.pack(pady=10, ipadx=10, ipady=5, fill="x", padx=40)

tk.Label(control_frame, text="Algorithm:", bg=PANEL_COLOR, fg=TEXT_COLOR, font=FONT)\
    .grid(row=0, column=0, padx=5)
alg_var = ttk.Combobox(control_frame, values=["BFS", "Dijkstra"], state="readonly", width=15)
alg_var.current(0)
alg_var.grid(row=0, column=1, padx=5)

tk.Label(control_frame, text="Map File:", bg=PANEL_COLOR, fg=TEXT_COLOR, font=FONT)\
    .grid(row=0, column=2, padx=5)
map_var = ttk.Combobox(
    control_frame,
    values=["DragonsAgeOrigins", "BauldersGateII"],
    state="readonly",
    width=20
)
map_var.current(0)
map_var.grid(row=0, column=3, padx=5)

run_btn = ttk.Button(
    control_frame, text="Run Algorithm",
    command=lambda: run_algorithm(alg_var.get(), map_var.get(), plot_frame, info_frame)
)
run_btn.grid(row=0, column=4, padx=10)

# Visualization area
plot_frame = tk.Frame(root, bg=BG_COLOR)
plot_frame.pack(pady=10)

# Info card (fixed size, visible always)
info_frame = tk.Frame(root, bg=PANEL_COLOR, bd=2, relief="ridge", height=140)
info_frame.pack(fill="x", padx=40, pady=20)
info_frame.pack_propagate(False)

placeholder = tk.Label(
    info_frame,
    text="Run an algorithm to see results.",
    font=("Consolas", 12),
    fg="#bbbbbb",
    bg=PANEL_COLOR,
    pady=20
)
placeholder.pack()

root.mainloop()
