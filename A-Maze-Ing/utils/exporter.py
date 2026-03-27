from core.maze import Maze
from core.solver import DFSSolver


def export_maze(maze: Maze, filename: str = "output.txt") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        for y in range(maze.height):
            for x in range(maze.width):
                val = maze.grid[y][x].walls.value & 0xF
                f.write(f"{val:X}")
            f.write("\n")

        f.write("\n")

        ex, ey = maze.entrypoint
        f.write(f"{ex},{ey}\n")

        sx, sy = maze.exitpoint
        f.write(f"{sx},{sy}\n")

        solver = DFSSolver(maze)
        if solver.solve():
            path_str = ""
            coords = solver.path
            for i in range(len(coords) - 1):
                p1 = coords[i]
                p2 = coords[i + 1]
                if p2[0] > p1[0]:
                    path_str += "E"
                elif p2[0] < p1[0]:
                    path_str += "W"
                elif p2[1] > p1[1]:
                    path_str += "S"
                elif p2[1] < p1[1]:
                    path_str += "N"
            f.write(path_str + "\n")
        else:
            f.write("None\n")
