from typing import Callable, Optional, Tuple, List
from core.maze import Maze, Direction, PathfindingState
from collections import deque


class MazeSolver:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze
        self.path: List[Tuple[int, int]] = []

    def solve(
            self,
            step_callback: Optional[Callable[[], None]] = None
    ) -> bool:
        raise NotImplementedError(
            "La méthode solve doit être implémentée par les sous-classes"
        )

    def _reset_states(self) -> None:
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                self.maze.grid[y][x].set_path_state(PathfindingState.UNVISITED)

    def _mark_path(
        self,
        path: List[Tuple[int, int]],
        step_callback: Optional[Callable[[], None]]
    ) -> None:
        for cy in range(self.maze.height):
            for cx in range(self.maze.width):
                cell = self.maze.grid[cy][cx]
                if cell.path_state in (
                    PathfindingState.VISITING,
                    PathfindingState.VISITED,
                ):
                    cell.set_path_state(PathfindingState.UNVISITED)
        for pt in path:
            self.maze.grid[pt[1]][pt[0]].set_path_state(PathfindingState.PATH)
            if step_callback:
                step_callback()

    def _get_neighbors(self, x: int, y: int) -> List[Tuple[int, int]]:
        cell = self.maze.grid[y][x]
        neighbors = []
        if (
            not cell.has_wall(Direction.N)
            and self.maze.is_valid_coordinate(x, y - 1)
        ):
            neighbors.append((x, y - 1))
        if (
            not cell.has_wall(Direction.E)
            and self.maze.is_valid_coordinate(x + 1, y)
        ):
            neighbors.append((x + 1, y))
        if (
            not cell.has_wall(Direction.S)
            and self.maze.is_valid_coordinate(x, y + 1)
        ):
            neighbors.append((x, y + 1))
        if (
            not cell.has_wall(Direction.W)
            and self.maze.is_valid_coordinate(x - 1, y)
        ):
            neighbors.append((x - 1, y))
        return neighbors


class BFSSolver(MazeSolver):
    def solve(
            self,
            step_callback: Optional[Callable[[], None]] = None
    ) -> bool:
        self._reset_states()
        start_pt = self.maze.entrypoint
        end_pt = self.maze.exitpoint
        if start_pt == (-1, -1) or end_pt == (-1, -1):
            return False

        queue: deque[Tuple[int, int, List[Tuple[int, int]]]] = deque(
            [(start_pt[0], start_pt[1], [])]
        )
        visited = {(start_pt[0], start_pt[1])}

        while queue:
            x, y, path = queue.popleft()
            self.maze.grid[y][x].set_path_state(PathfindingState.VISITING)
            current_path = path + [(x, y)]

            if (x, y) == end_pt:
                self.path = current_path
                self._mark_path(current_path, step_callback)
                return True

            for nx, ny in self._get_neighbors(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if step_callback:
                        step_callback()
                    queue.append((nx, ny, current_path))
            self.maze.grid[y][x].set_path_state(PathfindingState.VISITED)

        return False


class DFSSolver(MazeSolver):
    def solve(
            self,
            step_callback: Optional[Callable[[], None]] = None
    ) -> bool:
        self._reset_states()
        start_pt = self.maze.entrypoint
        end_pt = self.maze.exitpoint
        if start_pt == (-1, -1) or end_pt == (-1, -1):
            return False

        stack: List[Tuple[int, int, List[Tuple[int, int]]]] = [
            (start_pt[0], start_pt[1], [])
        ]
        visited = {(start_pt[0], start_pt[1])}

        while stack:
            x, y, path = stack.pop()
            self.maze.grid[y][x].set_path_state(PathfindingState.VISITING)
            current_path = path + [(x, y)]

            if (x, y) == end_pt:
                self.path = current_path
                self._mark_path(current_path, step_callback)
                return True

            for nx, ny in self._get_neighbors(x, y):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if step_callback:
                        step_callback()
                    stack.append((nx, ny, current_path))
            self.maze.grid[y][x].set_path_state(PathfindingState.VISITED)

        return False
