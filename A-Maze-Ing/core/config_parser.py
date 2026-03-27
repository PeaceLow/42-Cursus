import os
import sys

if __name__ == "__main__":
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    )

from utils.logger import logger
from typing import Any


def parse_config_line(line: str) -> tuple[str, str] | None:
    line = line.strip()

    if not line or line.startswith("#"):
        return None

    line = line.split("#", 1)[0].strip()

    if "=" not in line:
        logger.error(f"Ligne invalide ('=' manquant) : {line}")
        return None

    key, value = line.split("=", 1)
    key = key.strip()
    value = value.strip()

    if not key or not value:
        logger.error(f"Ligne invalide (clé ou valeur manquantes) : '{line}'")
        return None

    return key.upper(), value


def cast_value(key: str, raw_value: str, expected_type: type) -> Any:
    value = raw_value.strip().upper()
    try:
        if expected_type is bool:
            if value in ("TRUE", "YES", "1"):
                return True
            if value in ("FALSE", "NO", "0"):
                return False
            raise ValueError(f"'{key}' doit être 'true' ou 'false'")

        if expected_type is tuple:
            parts = [p.strip() for p in value.split(",")]
            if len(parts) != 2:
                raise ValueError(f"'{key}' doit être au format 'int,int'")
            return tuple(int(p) for p in parts)

        if expected_type is int:
            if not value.isdigit():
                raise ValueError(f"'{key}' doit être un entier")
            return int(value)

        return expected_type(raw_value.strip())

    except ValueError as e:
        logger.error(f"Valeur invalide: {e}")


def parse_config(
    file_name: str,
    required_keys: dict[str, type] | None = None,
    optional_keys: dict[str, type] | None = None,
) -> dict[str, Any]:
    required = required_keys or {}
    optional = optional_keys or {}
    types = {**required, **optional}

    config_data = {}

    try:
        with open(file_name, "r") as f:
            for line in f:
                parsed = parse_config_line(line)
                if not parsed:
                    continue

                key, raw_value = parsed

                if key in types:
                    config_data[key] = cast_value(key, raw_value, types[key])
                else:
                    config_data[key] = raw_value

    except FileNotFoundError:
        logger.error(f"Fichier de configuration introuvable : '{file_name}'")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erreur de lecture du fichier : {e}")
        sys.exit(1)

    missing_keys = [k for k in required if k not in config_data]
    if missing_keys:
        logger.error(f"Clés manquantes : {', '.join(missing_keys)}")
    logger.info(f"Configuration chargée avec succès depuis '{file_name}'")
    return config_data


_COLOR_KEYS = {
    "WALL_COLOR",
    "ENTRY_COLOR",
    "EXIT_COLOR",
    "TEMPLATE_COLOR",
    "SOLVED_PATH_COLOR",
    "SEARCH_PATH_COLOR",
    "VISITING_COLOR",
}


def _get_template_cells(width: int, height: int) -> set[tuple[int, int]]:
    from core.maze import MAZE_TEMPLATE

    tmpl_h = len(MAZE_TEMPLATE)
    tmpl_w = len(MAZE_TEMPLATE[0])
    cx = (width - tmpl_w) // 2
    cy = (height - tmpl_h) // 2
    cells: set[tuple[int, int]] = set()
    for row_i, row in enumerate(MAZE_TEMPLATE):
        for col_i, ch in enumerate(row):
            if ch == "1":
                cells.add((cx + col_i, cy + row_i))
    return cells


def _get_valid_color_pairs() -> set[int]:
    from display.ascii_viewer import VALID_COLOR_PAIRS

    return VALID_COLOR_PAIRS


def validate_config(config: dict[str, Any]) -> None:
    width: int = config.get("WIDTH", 0)
    height: int = config.get("HEIGHT", 0)

    if width < 1:
        logger.error(f"WIDTH={width} invalide : doit être >= 1")
    if height < 1:
        logger.error(f"HEIGHT={height} invalide : doit être >= 1")
    if width == 1 and height == 1:
        logger.error(
            "Taille 1x1 invalide : au moins une dimension"
            " doit être >= 2"
        )

    entry: tuple[int, int] | None = config.get("ENTRY")
    exit_pt: tuple[int, int] | None = config.get("EXIT")

    if entry is not None:
        ex, ey = entry
        if not (0 <= ex < width and 0 <= ey < height):
            logger.error(
                f"ENTRY={entry} hors des limites du labyrinthe"
                f" ({width}x{height})"
            )

    if exit_pt is not None:
        sx, sy = exit_pt
        if not (0 <= sx < width and 0 <= sy < height):
            logger.error(
                f"EXIT={exit_pt} hors des limites du labyrinthe"
                f" ({width}x{height})"
            )

    if entry is not None and exit_pt is not None and entry == exit_pt:
        logger.error(f"ENTRY et EXIT ne peuvent pas être identiques : {entry}")

    template_cells = _get_template_cells(width, height)
    if entry is not None and entry in template_cells:
        logger.error(f"ENTRY={entry} est sur une cellule template")
    if exit_pt is not None and exit_pt in template_cells:
        logger.error(f"EXIT={exit_pt} est sur une cellule template")

    valid_colors = _get_valid_color_pairs()
    for key in _COLOR_KEYS:
        if key in config and config[key] not in valid_colors:
            logger.warning(
                f"{key}={config[key]} invalide : doit être entre 1 et 8,"
                f" valeur ignorée."
            )
            del config[key]

    if "MAZE_STYLE" in config:
        if config["MAZE_STYLE"].lower() not in ("fin", "epais", "massif"):
            logger.warning(
                f"MAZE_STYLE='{config['MAZE_STYLE']}' invalide : doit être"
                f" 'fin', 'epais' ou 'massif', valeur ignorée."
            )
            del config["MAZE_STYLE"]

    if "DISPLAY" in config:
        if config["DISPLAY"].upper() != "ASCII":
            logger.warning(
                f"DISPLAY='{config['DISPLAY']}' invalide : doit être 'ASCII',"
                f" valeur ignorée."
            )
            del config["DISPLAY"]

    if "GENERATOR" in config:
        if config["GENERATOR"].upper() not in ("DFS", "PRIM", "KRUSKAL"):
            logger.warning(
                f"GENERATOR='{config['GENERATOR']}' invalide : doit être"
                f" 'DFS', 'PRIM' ou 'KRUSKAL', valeur ignorée."
            )
            del config["GENERATOR"]

    if "SOLVER" in config:
        if config["SOLVER"].upper() not in ("BFS", "DFS"):
            logger.warning(
                f"SOLVER='{config['SOLVER']}' invalide : doit être"
                f" 'BFS' ou 'DFS', valeur ignorée."
            )
            del config["SOLVER"]

    if "LOG_LEVEL" in config:
        if config["LOG_LEVEL"].upper() not in (
            "DEBUG", "INFO", "WARNING", "ERROR"
        ):
            logger.warning(
                f"LOG_LEVEL='{config['LOG_LEVEL']}' invalide, valeur ignorée."
            )
            del config["LOG_LEVEL"]


if __name__ == "__main__":
    config_file = "config.txt"
    logger.set_level("DEBUG")
    config = parse_config(
        config_file,
        required_keys={
            "WIDTH": int,
            "HEIGHT": int,
            "WALL_DENSITY": float,
            "OUTPUT_FILE": str,
        },
        optional_keys={"SEED": int, "LOG_LEVEL": str},
    )
    logger.info(f"Config loaded successfully from {config_file}")
    for key, value in config.items():
        logger.info(f"{key}: {value}")
