import argparse
from core.config_parser import parse_config, validate_config
from utils.logger import logger
from display.ascii_viewer import AsciiViewer
from display.base_viewer import BaseViewer
from controllers.maze_controller import MazeController


def create_viewer(display_type: str, controller: MazeController) -> BaseViewer:
    if display_type == "ASCII":
        return AsciiViewer(controller)
    else:
        raise ValueError(f"Viewer inconnu : {display_type}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A-Maze-ing: Maze Generator"
    )
    parser.add_argument(
        "config_file",
        help="Chemin vers le fichier de configuration (ex: config.txt)"
    )
    args = parser.parse_args()

    config = parse_config(
        args.config_file,
        required_keys={
            "WIDTH": int,
            "HEIGHT": int,
            "ENTRY": tuple,
            "EXIT": tuple,
            "OUTPUT_FILE": str,
            "PERFECT": bool,
        },
        optional_keys={
            "SEED": int,
            "LOG_LEVEL": str,
            "DISPLAY": str,
            "GENERATOR": str,
            "ANIMATION": bool,
            "MAZE_STYLE": str,
            "WALL_COLOR": int,
            "ENTRY_COLOR": int,
            "EXIT_COLOR": int,
            "TEMPLATE_COLOR": int,
            "SOLVED_PATH_COLOR": int,
            "SEARCH_PATH_COLOR": int,
            "VISITING_COLOR": int,
            "SOLVER": str,
        },
    )

    if "LOG_LEVEL" in config:
        logger.set_level(config["LOG_LEVEL"])

    validate_config(config)

    logger.info(f"Configuration chargée : {config}")

    controller = MazeController(config)

    try:
        viewer = create_viewer(config.get("DISPLAY", "ASCII"), controller)
        viewer.display()
    except Exception as e:
        logger.error(f"Erreur lors du lancement de l'affichage : {e}")


if __name__ == "__main__":
    main()
