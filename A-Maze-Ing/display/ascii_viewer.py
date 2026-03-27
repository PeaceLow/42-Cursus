import curses
import sys
from typing import Any, Dict, List, Optional, Tuple
from display.base_viewer import BaseViewer
from core.maze import Direction, CellType, Maze

VALID_COLOR_PAIRS: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}


STYLES: Dict[str, Dict[str, Any]] = {
    "fin": {
        "type": "line",
        "chars": [
            " ",
            "╵",
            "╶",
            "└",
            "╷",
            "│",
            "┌",
            "├",
            "╴",
            "┘",
            "─",
            "┴",
            "┐",
            "┤",
            "┬",
            "┼",
        ],
    },
    "epais": {
        "type": "line",
        "chars": [
            " ",
            "╹",
            "╺",
            "┗",
            "╻",
            "┃",
            "┏",
            "┣",
            "╸",
            "┛",
            "━",
            "┻",
            "┓",
            "┫",
            "┳",
            "╋",
        ],
    },
    "massif": {"type": "block", "wall": "█", "path": " "},
}


class AsciiViewer(BaseViewer):
    def __init__(self, controller: Any) -> None:
        super().__init__(controller)
        self.wall_color: int = controller.config.get("WALL_COLOR", 5)
        self.entry_color: int = controller.config.get("ENTRY_COLOR", 1)
        self.exit_color: int = controller.config.get("EXIT_COLOR", 2)
        self.template_color: int = controller.config.get("TEMPLATE_COLOR", 7)
        self.solved_path_color: int = controller.config.get(
            "SOLVED_PATH_COLOR", 8)
        self.search_path_color: int = controller.config.get(
            "SEARCH_PATH_COLOR", 4)
        self.visiting_color: int = controller.config.get("VISITING_COLOR", 10)
        self.maze_style: str = controller.config.get(
            "MAZE_STYLE", "fin").lower()
        self.show_path: bool = False
        self.animation: bool = controller.config.get("ANIMATION", False)
        self.animation_speed: str = "Normale"
        self.entry_char: str = controller.config.get("ENTRY_CHAR", "█")
        self.exit_char: str = controller.config.get("EXIT_CHAR", "█")
        self.maze_lines: List[str] = []
        self.color_grid: List[List[int]] = []
        self.menu_items: List[Dict[str, Any]] = []
        self.current_menu: List[Dict[str, Any]] = []
        self.current_selection: int = 0
        self.menu_stack: List[Tuple[List[Dict[str, Any]], int]] = []
        self.stdscr: Any = None
        self._init_menus()

    def _init_menus(self) -> None:
        def make_color_menu(attribute: str) -> List[Dict[str, Any]]:
            return [
                {
                    "label": "Blanc",
                    "action": lambda: self.set_color(attribute, 5),
                    "color_pair": 5,
                },
                {
                    "label": "Gris",
                    "action": lambda: self.set_color(attribute, 12),
                    "color_pair": 12,
                },
                {
                    "label": "Gris clair",
                    "action": lambda: self.set_color(attribute, 13),
                    "color_pair": 13,
                },
                {
                    "label": "Noir",
                    "action": lambda: self.set_color(attribute, 14),
                    "color_pair": 14,
                },
                {
                    "label": "Rouge",
                    "action": lambda: self.set_color(attribute, 2),
                    "color_pair": 2,
                },
                {
                    "label": "Orange",
                    "action": lambda: self.set_color(attribute, 9),
                    "color_pair": 9,
                },
                {
                    "label": "Jaune",
                    "action": lambda: self.set_color(attribute, 8),
                    "color_pair": 8,
                },
                {
                    "label": "Vert",
                    "action": lambda: self.set_color(attribute, 1),
                    "color_pair": 1,
                },
                {
                    "label": "Cyan",
                    "action": lambda: self.set_color(attribute, 3),
                    "color_pair": 3,
                },
                {
                    "label": "Bleu clair",
                    "action": lambda: self.set_color(attribute, 11),
                    "color_pair": 11,
                },
                {
                    "label": "Bleu",
                    "action": lambda: self.set_color(attribute, 4),
                    "color_pair": 4,
                },
                {
                    "label": "Magenta",
                    "action": lambda: self.set_color(attribute, 7),
                    "color_pair": 7,
                },
                {
                    "label": "Rose",
                    "action": lambda: self.set_color(attribute, 10),
                    "color_pair": 10,
                },
                {"label": "Retour", "action": "return"},
            ]

        def make_style_menu() -> List[Dict[str, Any]]:
            return [
                {"label": "Fin", "action": lambda: self.set_style("fin")},
                {"label": "Épais", "action": lambda: self.set_style("epais")},
                {
                    "label": "Massif",
                    "action": lambda: self.set_style("massif"),
                },
                {"label": "Retour", "action": "return"},
            ]

        def make_char_menu() -> List[Dict[str, Any]]:
            return [
                {
                    "label": "█ / █",
                    "action": lambda: self.set_entry_exit_chars("█", "█"),
                },
                {
                    "label": "S / E",
                    "action": lambda: self.set_entry_exit_chars("S", "E"),
                },
                {
                    "label": "I / O",
                    "action": lambda: self.set_entry_exit_chars("I", "O"),
                },
                {
                    "label": "A / B",
                    "action": lambda: self.set_entry_exit_chars("A", "B"),
                },
                {
                    "label": "★ / ☆",
                    "action": lambda: self.set_entry_exit_chars("★", "☆"),
                },
                {
                    "label": "● / ○",
                    "action": lambda: self.set_entry_exit_chars("●", "○"),
                },
                {"label": "Retour", "action": "return"},
            ]

        color_menu: List[Dict[str, Any]] = [
            {
                "label": "Couleur des murs",
                "submenu": make_color_menu("wall_color"),
            },
            {
                "label": "Couleur du logo",
                "submenu": make_color_menu("template_color"),
            },
            {
                "label": "Couleur de l'entrée",
                "submenu": make_color_menu("entry_color"),
            },
            {
                "label": "Couleur de la sortie",
                "submenu": make_color_menu("exit_color"),
            },
            {"label": "Retour", "action": "return"},
        ]

        personnalisation_menu: List[Dict[str, Any]] = [
            {"label": "Couleurs", "submenu": color_menu},
            {"label": "Style visuel", "submenu": make_style_menu()},
            {"label": "Style Entrée/Sortie", "submenu": make_char_menu()},
            {"label": "Retour", "action": "return"},
        ]

        def get_anim_label() -> str:
            return "Animation: " + (
                "Activée"
                if getattr(self, "animation", False)
                else "Désactivée"
            )

        def get_speed_label() -> str:
            spd = getattr(self, "animation_speed", "Normale")
            return f"Vitesse animation: {spd}"

        def get_perfect_label() -> str:
            return "Labyrinthe: " + (
                "Parfait"
                if self.controller.config.get("PERFECT", True)
                else "Imparfait"
            )

        menu_generator: List[Dict[str, Any]] = [
            {
                "label": "DFS",
                "action": lambda: self.action_change_type("DFS"),
            },
            {
                "label": "PRIM",
                "action": lambda: self.action_change_type("PRIM"),
            },
            {
                "label": "Kruskal",
                "action": lambda: self.action_change_type("KRUSKAL"),
            },
            {
                "label": "Retour",
                "action": "return",
            },
        ]

        menu_solver: List[Dict[str, Any]] = [
            {
                "label": "BFS",
                "action": lambda: self.action_change_solver_type("BFS"),
            },
            {
                "label": "DFS",
                "action": lambda: self.action_change_solver_type("DFS"),
            },
            {
                "label": "Retour",
                "action": "return",
            },
        ]

        parametres_menu: List[Dict[str, Any]] = [
            {
                "label": "Changer la taille",
                "action": self.action_interactive_resize,
            },
            {
                "label": "Changer Entrée/Sortie",
                "action": self.action_interactive_points,
            },
            {"label": get_anim_label, "action": self.action_toggle_animation},
            {"label": get_speed_label, "action": self.action_toggle_speed},
            {"label": get_perfect_label, "action": self.action_toggle_perfect},
            {
                "label": "Changer la seed",
                "action": self.action_change_seed,
                "prompts": ["Entrez la seed (vide pour aleatoire): "],
            },
            {
                "label": "Changer le genérateur",
                "submenu": menu_generator,
            },
            {
                "label": "Changer le solveur",
                "submenu": menu_solver,
            },
            {"label": "Retour", "action": "return"},
        ]

        self.menu_items = [
            {
                "label": "Regenerer le labyrinthe",
                "action": self.action_regenerate,
            },
            {"label": "Exporter le labyrinthe", "action": self.action_export},
            {"label": "Montrer le chemin", "action": self.action_show_path},
            {"label": "Paramètres du labyrinthe", "submenu": parametres_menu},
            {"label": "Personnalisation", "submenu": personnalisation_menu},
            {"label": "Quitter", "action": self.action_quit},
        ]
        self.current_menu = self.menu_items
        self.current_selection = 0
        self.menu_stack = []

    def action_regenerate(self) -> None:
        self.controller.generate_maze(animated=self.animation)

    def action_export(self) -> None:
        from utils.exporter import export_maze
        import os

        filename: str = self.controller.config.get("OUTPUT_FILE", "")
        if not filename:
            prompt_msg = "Nom fichier (defaut: output.txt): "
            filename = self.prompt_user_input(prompt_msg)
            if not filename.strip():
                filename = "output.txt"
        elif os.path.exists(filename):
            prompt_msg = f"Le fichier {filename} existe. Ecraser ? (o/N): "
            rep = self.prompt_user_input(prompt_msg)
            if rep.lower() != "o":
                self.show_message("Export annulé.")
                return

        if not self.controller.maze:
            self.show_message("Erreur: pas de labyrinthe a exporter.")
            return

        try:
            export_maze(self.controller.maze, filename)
            self.show_message(f"Labyrinthe exporté dans {filename}.")
        except Exception as e:
            self.show_message(f"Erreur d'export: {e}")

    def action_show_path(self) -> None:
        self.show_path = not self.show_path

        for item in self.menu_items:
            if item.get("action") == self.action_show_path:
                item["label"] = (
                    "Cacher le chemin"
                    if self.show_path
                    else "Montrer le chemin"
                )

        if not self.controller.maze:
            return

        if self.show_path:
            self.controller.solve_maze(animated=self.animation)
        else:
            self.controller.clear_solution()
            self._update_maze_lines()

    def action_change_type(self, maze_type: str) -> None:
        self.controller.change_type(maze_type)
        if self.menu_stack:
            self.current_menu, self.current_selection = self.menu_stack.pop()

    def action_change_solver_type(self, solver_type: str) -> None:
        self.controller.change_solver_type(solver_type)
        if self.show_path and self.controller.maze:
            self.controller.solve_maze(animated=self.animation)
        if self.menu_stack:
            self.current_menu, self.current_selection = self.menu_stack.pop()

    def action_quit(self) -> None:
        sys.exit(0)

    def action_toggle_animation(self) -> None:
        self.animation = not getattr(self, "animation", False)

    def action_toggle_speed(self) -> None:
        speeds = {"Lente": "Normale", "Normale": "Rapide", "Rapide": "Lente"}
        curr = getattr(self, "animation_speed", "Normale")
        self.animation_speed = speeds.get(curr, "Normale")

    def action_toggle_perfect(self) -> None:
        self.controller.config["PERFECT"] = not self.controller.config.get(
            "PERFECT", True
        )
        self.controller.generate_maze(animated=self.animation)

    def action_interactive_resize(self) -> None:
        from display.ascii_interactive import AsciiInteractiveConfig

        AsciiInteractiveConfig(self, self.controller).resize()

    def action_interactive_points(self) -> None:
        from display.ascii_interactive import AsciiInteractiveConfig

        AsciiInteractiveConfig(self, self.controller).set_points()

    def action_change_seed(self, seed_str: str) -> None:
        if not seed_str.strip():
            if "SEED" in self.controller.config:
                del self.controller.config["SEED"]
            import random

            random.seed()
        else:
            try:
                s = int(seed_str)
                self.controller.config["SEED"] = s
                import random

                random.seed(s)
            except ValueError:
                self.show_message("Seed invalide. Doit etre un nombre.")
                return
        self.controller.generate_maze()

    def set_color(self, target_attribute: str, color_id: int) -> None:
        setattr(self, target_attribute, color_id)
        self._update_maze_lines()
        if self.menu_stack:
            self.current_menu, self.current_selection = self.menu_stack.pop()

    def set_style(self, style_name: str) -> None:
        self.maze_style = style_name
        self._update_maze_lines()
        if self.menu_stack:
            self.current_menu, self.current_selection = self.menu_stack.pop()

    def set_entry_exit_chars(self, entry: str, exit_c: str) -> None:
        self.entry_char = entry
        self.exit_char = exit_c
        self._update_maze_lines()
        if self.menu_stack:
            self.current_menu, self.current_selection = self.menu_stack.pop()

    # ------------------------------------------------------------------
    # Handlers d'événements MVC
    # ------------------------------------------------------------------

    def on_maze_generated(self, **kwargs: Any) -> None:
        if (
            self.show_path
            and not self.controller.error_msg
            and self.controller.maze
        ):
            self.controller.solve_maze()
        else:
            self._update_maze_lines()

    def on_maze_step(self, **kwargs: Any) -> None:
        import time

        self._update_maze_lines()
        self._render_all()
        speed_map = {"Lente": 0.05, "Normale": 0.005, "Rapide": 0.0005}
        curr = getattr(self, "animation_speed", "Normale")
        delay = speed_map.get(curr, 0.005)
        time.sleep(delay)

    def on_solve_complete(self, **kwargs: Any) -> None:
        path_found = kwargs.get("path_found", True)
        self._update_maze_lines()
        if self.show_path and not path_found:
            self.show_path = False
            for item in self.menu_items:
                if item.get("action") == self.action_show_path:
                    item["label"] = "Montrer le chemin"
            self.show_message("Aucun chemin possible.")

    def on_solve_step(self, **kwargs: Any) -> None:
        import time

        self._update_maze_lines()
        self._render_all()
        speed_map = {"Lente": 0.05, "Normale": 0.005, "Rapide": 0.0005}
        curr = getattr(self, "animation_speed", "Normale")
        delay = speed_map.get(curr, 0.005)
        time.sleep(delay)

    def on_type_changed(self, **kwargs: Any) -> None:
        self._update_maze_lines()

    def on_error(self, **kwargs: Any) -> None:
        self._update_maze_lines()

    def _build_wall_grid(
        self, maze: Maze, w_ext: int, h_ext: int
    ) -> List[List[bool]]:
        grid = [[True for _ in range(w_ext)] for _ in range(h_ext)]
        for y in range(maze.height):
            for x in range(maze.width):
                cell = maze.grid[y][x]
                gx, gy = x * 2 + 1, y * 2 + 1
                grid[gy][gx] = False

                if not cell.has_wall(Direction.N) and y > 0:
                    grid[gy - 1][gx] = False
                if not cell.has_wall(Direction.E) and x < maze.width - 1:
                    grid[gy][gx + 1] = False
                if not cell.has_wall(Direction.S) and y < maze.height - 1:
                    grid[gy + 1][gx] = False
                if not cell.has_wall(Direction.W) and x > 0:
                    grid[gy][gx - 1] = False
        return grid

    def _get_pathfinding_status(
        self, maze: Maze, x: int, y: int, is_wall: bool
    ) -> Tuple[bool, bool, bool]:
        style_type = STYLES.get(self.maze_style, STYLES["fin"]).get("type")
        if is_wall or style_type == "block":
            return False, False, False

        from core.maze import PathfindingState

        maze_x_c = x // 2
        maze_y_c = y // 2
        is_path, is_visiting, is_visited = False, False, False

        def passage_states(
            s1: PathfindingState, s2: PathfindingState
        ) -> Tuple[bool, bool, bool]:
            path = s1 == PathfindingState.PATH and s2 == PathfindingState.PATH
            visiting = (
                s1 == PathfindingState.VISITING
                or s2 == PathfindingState.VISITING
            )
            visited = (
                not path
                and not visiting
                and (
                    s1 == PathfindingState.VISITED
                    or s2 == PathfindingState.VISITED
                )
            )
            return path, visiting, visited

        if x % 2 == 1 and y % 2 == 1:
            if 0 <= maze_x_c < maze.width and 0 <= maze_y_c < maze.height:
                state = maze.grid[maze_y_c][maze_x_c].path_state
                is_path = state == PathfindingState.PATH
                is_visiting = state == PathfindingState.VISITING
                is_visited = state == PathfindingState.VISITED
        elif x % 2 == 0 and y % 2 == 1:
            if 0 < maze_x_c < maze.width and 0 <= maze_y_c < maze.height:
                s1 = maze.grid[maze_y_c][maze_x_c - 1].path_state
                s2 = maze.grid[maze_y_c][maze_x_c].path_state
                is_path, is_visiting, is_visited = passage_states(s1, s2)
        elif x % 2 == 1 and y % 2 == 0:
            if 0 <= maze_x_c < maze.width and 0 < maze_y_c < maze.height:
                s1 = maze.grid[maze_y_c - 1][maze_x_c].path_state
                s2 = maze.grid[maze_y_c][maze_x_c].path_state
                is_path, is_visiting, is_visited = passage_states(s1, s2)

        return is_path, is_visiting, is_visited

    def _determine_char_and_color(
        self,
        x: int,
        y: int,
        grid: List[List[bool]],
        maze: Maze,
        w_ext: int,
        h_ext: int,
        style: Dict[str, Any],
    ) -> Tuple[str, bool, int]:
        is_wall = grid[y][x]
        maze_x = x // 2 if x % 2 != 0 else (x - 1) // 2
        maze_y = y // 2 if y % 2 != 0 else (y - 1) // 2

        cell_type = None
        if 0 <= maze_x < maze.width and 0 <= maze_y < maze.height:
            cell_type = maze.grid[maze_y][maze_x].type

        gx_entry = maze.entrypoint[0] * 2 + 1
        gy_entry = maze.entrypoint[1] * 2 + 1
        gx_exit = maze.exitpoint[0] * 2 + 1
        gy_exit = maze.exitpoint[1] * 2 + 1

        is_template = cell_type == CellType.TEMPLATE and not is_wall
        is_path, is_visiting, is_visited = self._get_pathfinding_status(
            maze, x, y, is_wall
        )

        char = ""
        is_special = False
        color = 0

        if x == gx_entry and y == gy_entry:
            char = getattr(self, "entry_char", "E")
            is_special = True
            color = self.entry_color
        elif x == gx_exit and y == gy_exit:
            char = getattr(self, "exit_char", "S")
            is_special = True
            color = self.exit_color
        elif is_template:
            char = "█"
            color = self.template_color
        elif not is_wall:
            if is_path:
                char = "●"
                is_special = True
                color = self.solved_path_color
            elif is_visiting:
                char = "●"
                is_special = True
                color = self.visiting_color
            elif is_visited:
                char = "●"
                is_special = True
                color = self.search_path_color
            else:
                char = style.get("path", " ")
        elif style.get("type") == "block":
            char = style.get("wall", "█")
            color = self.wall_color
        elif style.get("type") == "line":
            mask = 0
            if y > 0 and grid[y - 1][x]:
                mask += 1
            if x < w_ext - 1 and grid[y][x + 1]:
                mask += 2
            if y < h_ext - 1 and grid[y + 1][x]:
                mask += 4
            if x > 0 and grid[y][x - 1]:
                mask += 8

            char_list = style.get("chars", [])
            if isinstance(char_list, list) and mask < len(char_list):
                char = char_list[mask]
            else:
                char = " "
            color = self.wall_color

        return char, is_special, color

    def _update_maze_lines(self) -> None:
        """Traduit le labyrinthe brut en caractères ASCII"""
        if not self.controller.maze or self.controller.error_msg:
            self.maze_lines = []
            return

        maze: Maze = self.controller.maze
        style = STYLES.get(self.maze_style, STYLES["fin"])

        w_ext = 2 * maze.width + 1
        h_ext = 2 * maze.height + 1
        grid = self._build_wall_grid(maze, w_ext, h_ext)

        self.maze_lines = []
        self.color_grid = [[0 for _ in range(w_ext * 2)] for _ in range(h_ext)]

        for y in range(h_ext):
            line_str = ""
            for x in range(w_ext):
                char, is_special, color = self._determine_char_and_color(
                    x, y, grid, maze, w_ext, h_ext, style
                )

                repeat_count = 3 if x % 2 == 1 else 1

                for i in range(repeat_count):
                    col_index = len(line_str)
                    self.color_grid[y][col_index] = color

                    if is_special and repeat_count == 3:
                        if char == "█":
                            char_to_print = char
                        else:
                            char_to_print = char if i == 1 else " "
                    else:
                        char_to_print = char

                    line_str += char_to_print

            self.maze_lines.append(line_str)

    def init_colors(self) -> None:
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_GREEN, -1)
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, curses.COLOR_CYAN, -1)
        curses.init_pair(4, curses.COLOR_BLUE, -1)
        curses.init_pair(5, curses.COLOR_WHITE, -1)
        curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(7, curses.COLOR_MAGENTA, -1)
        curses.init_pair(8, curses.COLOR_YELLOW, -1)
        if curses.can_change_color() and curses.COLORS >= 16:
            curses.init_color(9, 1000, 500, 0)  # orange
            curses.init_color(10, 1000, 400, 700)  # rose
            curses.init_color(11, 400, 700, 1000)  # bleu clair
            curses.init_color(12, 500, 500, 500)  # gris
            curses.init_color(13, 750, 750, 750)  # gris clair
            curses.init_color(14, 0, 0, 0)  # noir
            curses.init_pair(9, 9, -1)
            curses.init_pair(10, 10, -1)
            curses.init_pair(11, 11, -1)
            curses.init_pair(12, 12, -1)
            curses.init_pair(13, 13, -1)
            curses.init_pair(14, 14, -1)
        else:
            curses.init_pair(9, curses.COLOR_RED, -1)
            curses.init_pair(10, curses.COLOR_MAGENTA, -1)
            curses.init_pair(11, curses.COLOR_CYAN, -1)
            curses.init_pair(12, curses.COLOR_WHITE, -1)
            curses.init_pair(13, curses.COLOR_WHITE, -1)
            curses.init_pair(14, curses.COLOR_BLACK, -1)

    def display(self) -> None:
        curses.wrapper(self.run_terminal_menu)

    def _render_all(
        self,
    ) -> Tuple[Optional[int], Optional[int], Optional[int]]:
        if not getattr(self, "stdscr", None):
            return None, None, None
        stdscr = self.stdscr
        stdscr.erase()
        max_y, max_x = stdscr.getmaxyx()
        menu_height = len(self.current_menu) + 4
        visible_maze_lines = max(0, max_y - menu_height)

        if self.controller.error_msg:
            stdscr.addstr(
                0,
                0,
                self.controller.error_msg,
                curses.color_pair(2) | curses.A_BOLD,
            )
            lines_count = 2
        else:
            self._draw_maze(stdscr, visible_maze_lines, max_x)
            lines_count = len(self.maze_lines)

        start_y = min(lines_count, visible_maze_lines) + 1
        box_start_x = 2
        menu_width = max(
            34,
            max(
                [
                    len(
                        item.get("label", "")()
                        if callable(item.get("label", ""))
                        else item.get("label", "")
                    )
                    for item in self.current_menu
                ]
            )
            + 8,
        )
        self._draw_menu(stdscr, start_y, box_start_x, menu_width)

        stdscr.refresh()
        return start_y, box_start_x, menu_width

    def run_terminal_menu(self, stdscr: Any) -> None:
        self.stdscr = stdscr
        curses.curs_set(0)
        self.init_colors()
        stdscr.bkgd(" ", curses.color_pair(0))
        stdscr.keypad(True)
        curses.mousemask(
            curses.ALL_MOUSE_EVENTS | curses.REPORT_MOUSE_POSITION)

        self.action_regenerate()

        while True:
            start_y, box_start_x, menu_width = self._render_all()

            if start_y is None or box_start_x is None or menu_width is None:
                break

            if not self._handle_input(start_y, box_start_x, menu_width):
                break

    def _draw_maze(
        self, stdscr: Any, visible_lines: int, max_x: int
    ) -> None:
        for y, line in enumerate(self.maze_lines):
            if y >= visible_lines:
                break
            x_pos = 0
            for char in line:
                if x_pos >= max_x - 1:
                    break
                if (
                    y < len(self.color_grid)
                    and x_pos < len(self.color_grid[y])
                ):
                    color = self.color_grid[y][x_pos]
                else:
                    color = 0

                try:
                    stdscr.addstr(y, x_pos, char, curses.color_pair(color))
                except curses.error:
                    pass
                x_pos += 1

    def _draw_menu(
        self, stdscr: Any, start_y: int, box_start_x: int, menu_width: int
    ) -> None:
        try:
            title = (
                " Menu Principal "
                if not self.menu_stack
                else " Sous-Menu "
            )
            stdscr.addstr(
                start_y,
                box_start_x,
                "╭" + "─" * (menu_width - 2) + "╮",
                curses.color_pair(4),
            )
            title_pos = box_start_x + (menu_width - len(title)) // 2
            stdscr.addstr(
                start_y,
                title_pos,
                title,
                curses.A_BOLD | curses.color_pair(11)
            )
            stdscr.addstr(
                start_y + 1,
                box_start_x,
                "│" + " " * (menu_width - 2) + "│",
                curses.color_pair(4),
            )

            for idx, item in enumerate(self.current_menu):
                raw_label = item.get("label", "")
                label = raw_label() if callable(raw_label) else raw_label
                c_pair = item.get("color_pair", 5)
                stdscr.addstr(
                    start_y + 2 + idx,
                    box_start_x,
                    "│",
                    curses.color_pair(4)
                )

                if idx == self.current_selection:
                    text = f" ▶ {label} "
                    attr = curses.color_pair(6) | curses.A_BOLD
                else:
                    text = f"   {label} "
                    attr = curses.color_pair(c_pair)

                stdscr.addstr(
                    start_y + 2 + idx,
                    box_start_x + 1,
                    text.ljust(menu_width - 2),
                    attr,
                )
                stdscr.addstr(
                    start_y + 2 + idx,
                    box_start_x + menu_width - 1,
                    "│",
                    curses.color_pair(4),
                )

            last_y = start_y + 2 + len(self.current_menu)
            stdscr.addstr(
                last_y,
                box_start_x,
                "│" + " " * (menu_width - 2) + "│",
                curses.color_pair(4),
            )
            stdscr.addstr(
                last_y + 1,
                box_start_x,
                "╰" + "─" * (menu_width - 2) + "╯",
                curses.color_pair(4),
            )

            menu_labels = [
                (
                    item.get("label", "")()
                    if callable(item.get("label", ""))
                    else item.get("label", "")
                )
                for item in self.current_menu
            ]
            if "Changer la seed" in menu_labels:
                current_seed = self.controller.config.get("SEED", "Aléatoire")
                seed_msg = f" Seed actuelle : {current_seed} "
                stdscr.addstr(
                    start_y + 2,
                    box_start_x + menu_width + 2,
                    seed_msg,
                    curses.color_pair(8) | curses.A_BOLD,
                )
            if "Changer le genérateur" in menu_labels:
                current_gen = self.controller.config.get("GENERATOR", "DFS")
                gen_msg = f" Générateur : {current_gen} "
                stdscr.addstr(
                    start_y + 3,
                    box_start_x + menu_width + 2,
                    gen_msg,
                    curses.color_pair(8) | curses.A_BOLD,
                )
            if "Changer le solveur" in menu_labels:
                current_solver = self.controller.config.get("SOLVER", "BFS")
                solver_msg = f" Solveur : {current_solver} "
                stdscr.addstr(
                    start_y + 4,
                    box_start_x + menu_width + 2,
                    solver_msg,
                    curses.color_pair(8) | curses.A_BOLD,
                )

        except curses.error:
            pass

    def _handle_input(
        self, start_y: int, box_start_x: int, menu_width: int
    ) -> bool:
        if not self.stdscr:
            return True
        try:
            key = self.stdscr.getch()
        except curses.error:
            return True

        if key == curses.KEY_UP:
            if self.current_menu:
                self.current_selection = (self.current_selection - 1) % len(
                    self.current_menu
                )
        elif key == curses.KEY_DOWN:
            if self.current_menu:
                self.current_selection = (self.current_selection + 1) % len(
                    self.current_menu
                )
        elif key in [curses.KEY_ENTER, 10, 13]:
            return self.execute_menu_action()
        elif key == curses.KEY_MOUSE:
            try:
                _, mx, my, _, bstate = curses.getmouse()
                menu_start_y = start_y + 2
                menu_end_y = menu_start_y + len(self.current_menu)

                if (
                    menu_start_y <= my < menu_end_y
                    and box_start_x <= mx <= box_start_x + menu_width
                ):
                    self.current_selection = my - menu_start_y
                    click_flags = (
                        curses.BUTTON1_CLICKED
                        | curses.BUTTON1_DOUBLE_CLICKED
                        | curses.BUTTON1_RELEASED
                    )
                    if bstate & click_flags:
                        return self.execute_menu_action()
            except curses.error:
                pass
        return True

    def execute_menu_action(self) -> bool:
        if not self.current_menu:
            return True
        selected_item = self.current_menu[self.current_selection]
        if "submenu" in selected_item:
            self.menu_stack.append((self.current_menu, self.current_selection))
            self.current_menu = selected_item["submenu"]
            self.current_selection = 0
            return True

        selected_action = selected_item.get("action")
        if selected_action == "return":
            if self.menu_stack:
                popped = self.menu_stack.pop()
                self.current_menu, self.current_selection = popped
                return True
            return False

        if not selected_action or not callable(selected_action):
            return True

        prompts = selected_item.get("prompts", [])
        args = [self.prompt_user_input(p) for p in prompts]

        if args:
            selected_action(*args)
        else:
            selected_action()
        return True

    def prompt_user_input(self, prompt_text: str) -> str:
        if not self.stdscr:
            return ""
        curses.curs_set(1)
        curses.echo()
        max_y, max_x = self.stdscr.getmaxyx()
        self.stdscr.addstr(
            max_y - 2, 0, prompt_text + " " * (max_x - len(prompt_text) - 1)
        )
        self.stdscr.refresh()
        input_bytes = self.stdscr.getstr(max_y - 2, len(prompt_text))
        curses.curs_set(0)
        curses.noecho()
        try:
            return str(input_bytes.decode("utf-8"))
        except UnicodeDecodeError:
            return ""

    def show_message(self, msg: str) -> None:
        if not self.stdscr:
            return
        self.stdscr.clear()
        self.stdscr.addstr(msg)
        self.stdscr.addstr("\nAppuyez sur une touche pour continuer...")
        self.stdscr.refresh()
        self.stdscr.getch()

    def close(self) -> None:
        pass
