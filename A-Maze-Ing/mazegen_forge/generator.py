import random
from typing import Callable, Optional
from mazegen_forge.maze import Maze, CellType, Direction, OPPOSITE


class MazeGenerator:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze

    def generate(
            self,
            step_callback: Optional[Callable[[], None]] = None,
            perfect: bool = True) -> None:
        raise NotImplementedError(
            "La méthode generate doit être implémentée"
            " par les sous-classes")

    def _make_imperfect(
            self,
            step_callback: Optional[Callable[[], None]] = None) -> None:
        maze = self.maze

        candidates = [
            (x, y, d, nx, ny)
            for y in range(maze.height)
            for x in range(maze.width)
            if maze.grid[y][x].type != CellType.TEMPLATE
            for d, nx, ny in (
                (Direction.E, x + 1, y),
                (Direction.S, x, y + 1),
            )
            if maze.is_valid_coordinate(nx, ny)
            and maze.grid[ny][nx].type != CellType.TEMPLATE
            and maze.grid[y][x].has_wall(d)
        ]
        random.shuffle(candidates)

        removed = 0
        for x, y, direction, nx, ny in candidates:
            if removed >= max(1, len(candidates) // 6):
                break
            cell, nb = maze.grid[y][x], maze.grid[ny][nx]
            cell.remove_wall(direction)
            nb.remove_wall(OPPOSITE[direction])
            if self._has_2x2_open(x, y) or self._has_2x2_open(nx, ny):
                cell.walls |= direction
                nb.walls |= OPPOSITE[direction]
            else:
                removed += 1
                if step_callback:
                    step_callback()

    def _has_2x2_open(self, cx: int, cy: int) -> bool:
        maze = self.maze
        for ox in range(max(0, cx - 1), min(cx, maze.width - 2) + 1):
            for oy in range(max(0, cy - 1), min(cy, maze.height - 2) + 1):
                if all(
                    maze.grid[r][c].type != CellType.TEMPLATE
                    and (
                        c == ox + 1
                        or not maze.grid[r][c].has_wall(Direction.E)
                    )
                    and (
                        r == oy + 1
                        or not maze.grid[r][c].has_wall(Direction.S)
                    )
                    for r in range(oy, oy + 2)
                    for c in range(ox, ox + 2)
                ):
                    return True
        return False

    def _get_neighbor_coordinates(
            self,
            x: int,
            y: int,
            direction: Direction) -> tuple[int, int]:
        if direction == Direction.N:
            return x, y - 1
        elif direction == Direction.E:
            return x + 1, y
        elif direction == Direction.S:
            return x, y + 1
        elif direction == Direction.W:
            return x - 1, y
        else:
            raise ValueError(f"Direction invalide : {direction}")


class DFSGenerator(MazeGenerator):
    def generate(
            self,
            step_callback: Optional[Callable[[], None]] = None,
            perfect: bool = True) -> None:
        start_x, start_y = self.maze.entrypoint

        stack = [(start_x, start_y)]
        self.maze.grid[start_y][start_x].set_visited(True)
        if step_callback:
            step_callback()

        while stack:
            x, y = stack[-1]
            current_cell = self.maze.grid[y][x]

            directions = [Direction.N, Direction.E, Direction.S, Direction.W]
            random.shuffle(directions)

            moved = False
            for direction in directions:
                nx, ny = x, y
                if direction == Direction.N:
                    ny -= 1
                elif direction == Direction.E:
                    nx += 1
                elif direction == Direction.S:
                    ny += 1
                elif direction == Direction.W:
                    nx -= 1

                if self.maze.is_valid_coordinate(nx, ny):
                    next_cell = self.maze.grid[ny][nx]
                    if (
                        not next_cell.visited
                        and next_cell.type != CellType.TEMPLATE
                    ):
                        current_cell.remove_wall(direction)
                        next_cell.remove_wall(OPPOSITE[direction])
                        next_cell.set_visited(True)
                        if step_callback:
                            step_callback()
                        stack.append((nx, ny))
                        moved = True
                        break

            if not moved:
                stack.pop()

        if not perfect:
            self._make_imperfect(step_callback)


class PrimGenerator(MazeGenerator):
    def generate(
            self,
            step_callback: Optional[Callable[[], None]] = None,
            perfect: bool = True) -> None:
        start_x, start_y = self.maze.entrypoint
        self.maze.grid[start_y][start_x].set_visited(True)

        walls: list[tuple[int, int, Direction]] = []
        self._add_walls_available(start_x, start_y, walls)

        while walls:
            idx = random.randint(0, len(walls) - 1)
            x, y, direction = walls.pop(idx)
            nx, ny = self._get_neighbor_coordinates(x, y, direction)

            if self.maze.is_valid_coordinate(nx, ny):
                next_cell = self.maze.grid[ny][nx]
                if (not next_cell.visited and
                        next_cell.type != CellType.TEMPLATE):
                    self.maze.grid[y][x].remove_wall(direction)
                    next_cell.remove_wall(OPPOSITE[direction])
                    next_cell.set_visited(True)
                    if step_callback:
                        step_callback()
                    self._add_walls_available(nx, ny, walls)

        if not perfect:
            self._make_imperfect(step_callback)

    def _add_walls_available(
            self,
            x: int,
            y: int,
            walls: list[tuple[int, int, Direction]]) -> None:
        maze = self.maze
        for direction in [
            Direction.N, Direction.E, Direction.S, Direction.W
        ]:
            nx, ny = self._get_neighbor_coordinates(x, y, direction)

            if maze.is_valid_coordinate(nx, ny):
                next_cell = maze.grid[ny][nx]
                if (
                    not next_cell.visited
                    and next_cell.type != CellType.TEMPLATE
                ):
                    walls.append((x, y, direction))


class KruskalGenerator(MazeGenerator):
    def generate(
            self, step_callback: Optional[Callable[[], None]] = None,
            perfect: bool = True) -> None:

        width, height = self.maze.width, self.maze.height

        parents = {}
        walls = []
        for y in range(height):
            for x in range(width):
                if self.maze.grid[y][x].type != CellType.TEMPLATE:
                    parents[(x, y)] = (x, y)

        def find(cell: tuple[int, int]) -> tuple[int, int]:
            while parents[cell] != cell:
                parents[cell] = parents[parents[cell]]
                cell = parents[cell]
            return cell

        for y in range(height):
            for x in range(width):
                if self.maze.grid[y][x].type != CellType.TEMPLATE:
                    if (x < width - 1 and
                            self.maze.grid[y][x + 1].type
                            != CellType.TEMPLATE):
                        walls.append((x, y, Direction.E))
                    if (y < height - 1 and
                            self.maze.grid[y + 1][x].type
                            != CellType.TEMPLATE):
                        walls.append((x, y, Direction.S))
        random.shuffle(walls)

        for x, y, direction in walls:
            nx, ny = self._get_neighbor_coordinates(x, y, direction)
            if (self.maze.is_valid_coordinate(nx, ny)
                    and self.maze.grid[ny][nx].type != CellType.TEMPLATE):
                cell1 = find((x, y))
                cell2 = find((nx, ny))
                if cell1 != cell2:
                    self.maze.grid[y][x].remove_wall(direction)
                    self.maze.grid[ny][nx].remove_wall(OPPOSITE[direction])
                    parents[cell2] = cell1
                    if step_callback:
                        step_callback()

        if not perfect:
            self._make_imperfect(step_callback)
