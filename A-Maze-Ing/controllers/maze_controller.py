import random
from typing import Any, Dict, Optional

from core.maze import Maze, PathfindingState
from core.generator import DFSGenerator, MazeGenerator
from core.solver import MazeSolver, BFSSolver
from utils.observer import EventBus, MazeEvent


class MazeController:
    def __init__(
        self,
        config: Dict[str, Any],
        maze: Optional[Maze] = None,
        generator: Optional[MazeGenerator] = None,
    ) -> None:
        self.config = config
        self.maze = maze
        self.generator: Optional[MazeGenerator] = generator
        self.error_msg: Optional[str] = None
        self.events = EventBus()

    # ------------------------------------------------------------------
    # Génération
    # ------------------------------------------------------------------

    def generate_maze(self, animated: bool = False) -> None:
        try:
            if "SEED" in self.config:
                random.seed(self.config["SEED"])
            else:
                random.seed()

            width = self.config["WIDTH"]
            height = self.config["HEIGHT"]
            entry = self.config["ENTRY"]
            exit_pt = self.config["EXIT"]

            self.maze = Maze(width, height, entry, exit_pt)
            self._setup_generator(self.config.get("GENERATOR", "DFS"))

            step_cb = None
            if animated:

                def _gen_step() -> None:
                    self.events.emit(MazeEvent.MAZE_STEP)

                step_cb = _gen_step

            if self.generator:
                perfect = self.config.get("PERFECT", True)
                self.generator.generate(step_cb, perfect=perfect)

            self.error_msg = None
            self.events.emit(MazeEvent.MAZE_GENERATED)
        except Exception as e:
            self.error_msg = f"Erreur de génération : {e}"
            self.events.emit(MazeEvent.ERROR, message=str(e))

    # ------------------------------------------------------------------
    # Résolution
    # ------------------------------------------------------------------

    def solve_maze(self, animated: bool = False) -> bool:
        if not self.maze:
            return False

        step_cb = None
        if animated:

            def _solve_step() -> None:
                self.events.emit(MazeEvent.SOLVE_STEP)

            step_cb = _solve_step

        solver = self._create_solver()
        result = solver.solve(step_callback=step_cb)
        self.events.emit(MazeEvent.SOLVE_COMPLETE, path_found=result)
        return result

    def _create_solver(self) -> MazeSolver:
        if self.maze is None:
            raise ValueError("Maze n'est pas initialisé")
        solver_type = self.config.get("SOLVER", "BFS").upper()
        if solver_type == "BFS":
            return BFSSolver(self.maze)
        elif solver_type == "DFS":
            from core.solver import DFSSolver

            return DFSSolver(self.maze)
        else:
            raise ValueError(f"Solveur inconnu : {solver_type}")

    def change_solver_type(self, solver_type: str) -> None:
        self.config["SOLVER"] = solver_type.upper().strip()

    def clear_solution(self) -> None:
        if not self.maze:
            return
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                self.maze.grid[y][x].set_path_state(PathfindingState.UNVISITED)

    # ------------------------------------------------------------------
    # Configuration du générateur
    # ------------------------------------------------------------------

    def change_type(self, generator_type: str) -> None:
        self.config["GENERATOR"] = generator_type.upper().strip()
        if self.maze is None:
            raise ValueError("Maze n'est pas initialisé")
        self._setup_generator(generator_type)
        self.events.emit(MazeEvent.TYPE_CHANGED, generator_type=generator_type)

    def _setup_generator(self, generator_type: str) -> None:
        if self.maze is None:
            raise ValueError("Maze n'est pas initialisé")
        if generator_type.upper() == "DFS":
            self.generator = DFSGenerator(self.maze)
        elif generator_type.upper() == "PRIM":
            from core.generator import PrimGenerator

            self.generator = PrimGenerator(self.maze)
        elif generator_type.upper() == "KRUSKAL":
            from core.generator import KruskalGenerator

            self.generator = KruskalGenerator(self.maze)
        else:
            raise ValueError(f"Générateur inconnu : {generator_type}")
