"""
mazegen-forge
=============
Standalone maze generation and solving library.
"""
import random
from typing import List, Optional, Tuple

from mazegen_forge.maze import (
    Maze,
    Cell,
    Direction,
    CellType,
    PathfindingState,
    OPPOSITE,
)
from mazegen_forge.generator import (
    MazeGenerator,
    DFSGenerator,
    PrimGenerator,
    KruskalGenerator,
)
from mazegen_forge.solver import (
    MazeSolver,
    BFSSolver,
    DFSSolver,
)

__all__ = [
    # maze primitives
    "Maze",
    "Cell",
    "Direction",
    "CellType",
    "PathfindingState",
    "OPPOSITE",
    # generators
    "MazeGenerator",
    "DFSGenerator",
    "PrimGenerator",
    "KruskalGenerator",
    # solvers
    "MazeSolver",
    "BFSSolver",
    "DFSSolver",
    # convenience
    "generate",
    "solve",
]

_GENERATORS = {
    "DFS": DFSGenerator,
    "PRIM": PrimGenerator,
    "KRUSKAL": KruskalGenerator,
}

_SOLVERS = {
    "BFS": BFSSolver,
    "DFS": DFSSolver,
}


def generate(
    width: int,
    height: int,
    entry: Tuple[int, int] = (0, 0),
    exit_: Optional[Tuple[int, int]] = None,
    seed: Optional[int] = None,
    algorithm: str = "DFS",
    perfect: bool = True,
) -> Maze:
    """Create and return a fully generated :class:`Maze`.

    Parameters
    ----------
    width, height:
        Dimensions in cells (minimum 3×3 recommended).
    entry:
        (x, y) coordinates of the entry point. Defaults to top-left.
    exit_:
        (x, y) coordinates of the exit point. Defaults to bottom-right.
    seed:
        Integer seed for reproducible generation. ``None`` for random.
    algorithm:
        ``"DFS"`` (default), ``"PRIM"``, or ``"KRUSKAL"``.
    perfect:
        ``True`` for a perfect maze (no loops); ``False`` removes some walls.
    """
    if exit_ is None:
        exit_ = (width - 1, height - 1)

    if seed is not None:
        random.seed(seed)
    else:
        random.seed()

    maze = Maze(width, height, entry, exit_)
    gen_class = _GENERATORS.get(algorithm.upper(), DFSGenerator)
    gen_class(maze).generate(perfect=perfect)
    return maze


def solve(maze: Maze, algorithm: str = "BFS") -> List[Tuple[int, int]]:
    """Solve *maze* and return the solution path as a list of (x, y) tuples.

    Returns an empty list if no path exists.

    Parameters
    ----------
    maze:
        A :class:`Maze` instance (already generated).
    algorithm:
        ``"BFS"`` (default, shortest path) or ``"DFS"``.
    """
    solver_class = _SOLVERS.get(algorithm.upper(), BFSSolver)
    solver = solver_class(maze)
    found = solver.solve()
    return solver.path if found else []
