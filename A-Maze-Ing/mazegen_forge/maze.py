from typing import Any, Callable, Tuple, List, Set
from enum import Enum, IntFlag
from mazegen_forge._logger import logger

MAZE_TEMPLATE: List[str] = [
    "1000111",
    "1000001",
    "1110111",
    "0010100",
    "0010111",
]


class Direction(IntFlag):
    N = 1
    E = 2
    S = 4
    W = 8


OPPOSITE = {
    Direction.N: Direction.S,
    Direction.S: Direction.N,
    Direction.E: Direction.W,
    Direction.W: Direction.E,
}


class CellType(Enum):
    NORMAL = 0
    ENTRYPOINT = 1
    EXITPOINT = 2
    TEMPLATE = 3


class PathfindingState(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2
    PATH = 3


class Cell:
    def __init__(
        self,
        x: int,
        y: int,
        cell_type: CellType = CellType.NORMAL,
        visited: bool = False,
    ) -> None:
        self.x = x
        self.y = y
        self.walls: Direction = (
            Direction.N | Direction.E | Direction.S | Direction.W
        )
        self.type = cell_type
        self.visited = visited
        self.path_state: PathfindingState = PathfindingState.UNVISITED

    def set_visited(self, visited: bool = True) -> None:
        self.visited = visited

    def set_type(self, cell_type: CellType) -> None:
        self.type = cell_type

    def set_path_state(
        self, path_state: PathfindingState = PathfindingState.UNVISITED
    ) -> None:
        self.path_state = path_state

    def set_wall(self, bitmask: int, visited: bool | None = None) -> None:
        self.walls = Direction(bitmask)
        if visited is not None:
            self.set_visited(visited)

    def remove_wall(self, direction: Direction) -> None:
        self.walls &= ~direction

    def has_wall(self, direction: Direction) -> bool:
        return bool(self.walls & direction)


def CheckTemplateFit(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(
            self: Any, template: List[str], *args: Any, **kwargs: Any
    ) -> Any:
        if not template or not template[0]:
            logger.warning("Template vide ou invalide")
            return None
        template_height = len(template)
        template_width = len(template[0])
        if any(len(row) != template_width for row in template):
            logger.warning("Template non rectangulaire")
            return None
        if template_width >= self.width or template_height >= self.height:
            logger.warning("Template trop grand pour le labyrinthe")
            return None
        return func(self, template, *args, **kwargs)

    return wrapper


class Maze:
    def __init__(
        self,
        width: int,
        height: int,
        entrypoint: Tuple[int, int],
        exitpoint: Tuple[int, int],
    ) -> None:
        self.width = width
        self.height = height
        self.grid: list[list[Cell]] = [
            [Cell(x, y) for x in range(self.width)] for y in range(self.height)
        ]
        self.set_entrypoint(*entrypoint)
        self.set_exitpoint(*exitpoint)
        self.generate_empty_grid()

    def is_valid_coordinate(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def _set_special_point(
        self, x: int, y: int, cell_type: CellType
    ) -> Tuple[int, int]:
        if not self.is_valid_coordinate(x, y):
            logger.error("Coordonnées du point hors limites du labyrinthe")
            return (-1, -1)
        self.grid[y][x].set_type(cell_type)
        return (x, y)

    def set_entrypoint(self, x: int, y: int) -> None:
        self.entrypoint = self._set_special_point(x, y, CellType.ENTRYPOINT)

    def set_exitpoint(self, x: int, y: int) -> None:
        self.exitpoint = self._set_special_point(x, y, CellType.EXITPOINT)

    def remove_wall(self, cell1: Cell, cell2: Cell) -> None:
        if cell1.x == cell2.x:
            if cell1.y < cell2.y:
                self.remove_wall_by_direction(cell1, Direction.S)
            else:
                self.remove_wall_by_direction(cell1, Direction.N)
        elif cell1.y == cell2.y:
            if cell1.x < cell2.x:
                self.remove_wall_by_direction(cell1, Direction.E)
            else:
                self.remove_wall_by_direction(cell1, Direction.W)

    def remove_wall_by_direction(
            self, cell: Cell, direction: Direction) -> None:
        cell.remove_wall(direction)
        nx, ny = cell.x, cell.y
        if direction == Direction.N:
            ny -= 1
        elif direction == Direction.E:
            nx += 1
        elif direction == Direction.S:
            ny += 1
        elif direction == Direction.W:
            nx -= 1
        if self.is_valid_coordinate(nx, ny):
            self.grid[ny][nx].remove_wall(OPPOSITE[direction])

    @CheckTemplateFit
    def set_template(self, template: List[str]) -> None:
        centre_x = (self.width - len(template[0])) // 2
        centre_y = (self.height - len(template)) // 2
        for y, row in enumerate(template):
            for x, cell in enumerate(row):
                tmp = self.grid[centre_y + y][centre_x + x]
                if cell == "1":
                    tmp.set_type(CellType.TEMPLATE)
                    tmp.set_visited(True)

    def set_42template(self) -> None:
        self.set_template(MAZE_TEMPLATE)

    def generate_empty_grid(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x].set_wall(0b1111, visited=False)
                if (x, y) == self.entrypoint:
                    self.grid[y][x].set_type(CellType.ENTRYPOINT)
                elif (x, y) == self.exitpoint:
                    self.grid[y][x].set_type(CellType.EXITPOINT)
        self.set_42template()

    def _get_cell_hex_value(self, cell: Cell) -> str:
        return f"{cell.walls.value:X}"

    def generate_output(self) -> str:
        result = ""
        for y in range(self.height):
            row_string = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                row_string += self._get_cell_hex_value(cell)
            result += row_string + "\n"
        return result

    def get_visited_cells(self) -> Set[Tuple[int, int]]:
        visited = set()
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[y][x]
                if cell.visited:
                    visited.add((x, y))
        return visited

    @classmethod
    def load_from_string(
        cls,
        maze_string: str,
        entrypoint: Tuple[int, int],
        exitpoint: Tuple[int, int],
    ) -> "Maze":
        lines = maze_string.strip().splitlines()
        height = len(lines)
        width = len(lines[0]) if height > 0 else 0
        maze = cls(width, height, entrypoint, exitpoint)
        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                cell = maze.grid[y][x]
                cell.set_wall(int(char, 16), visited=True)
        return maze
