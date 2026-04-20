from pathlib import Path
from typing import Any, Dict, List, Optional
import sys


class MapParser:
    """
    Class responsible for discovering and parsing map files.
    """

    def __init__(self, maps_dir: str = "maps") -> None:
        """
        Initialize the MapParser.

        Args:
            maps_dir (str): The root directory to search for map files.
        """
        self.maps_dir: Path = Path(maps_dir)

    def list_map_files(self) -> List[Path]:
        """
        List all .txt map files in the given directory and its subdirectories.

        Returns:
            List[Path]: A list of paths to the map files.
        """
        return list(self.maps_dir.rglob("*.txt"))

    def parse_map_file(self, filepath: Path) -> Dict[str, Any]:
        """
        Parse a map file and extract its information.

        Args:
            filepath (Path): The path to the map file.

        Returns:
            Dict[str, Any]: A dictionary containing the extracted map info.
        """
        map_data: Dict[str, Any] = {
            "nb_drones": 0,
            "start_hub": None,
            "end_hub": None,
            "hubs": [],
            "connections": [],
        }

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue

                    if line.startswith("nb_drones:"):
                        val = line.split(":")[1].strip()
                        map_data["nb_drones"] = int(val)
                    elif line.startswith("start_hub:"):
                        parts = line.split(":", 1)[1].strip().split()
                        name, x, y = parts[0], int(parts[1]), int(parts[2])
                        options = " ".join(parts[3:]) if len(parts) > 3 else ""
                        map_data["start_hub"] = {
                            "name": name,
                            "x": x,
                            "y": y,
                            "options": options,
                        }
                    elif line.startswith("end_hub:"):
                        parts = line.split(":", 1)[1].strip().split()
                        name, x, y = parts[0], int(parts[1]), int(parts[2])
                        options = " ".join(parts[3:]) if len(parts) > 3 else ""
                        map_data["end_hub"] = {
                            "name": name,
                            "x": x,
                            "y": y,
                            "options": options,
                        }
                    elif line.startswith("hub:"):
                        parts = line.split(":", 1)[1].strip().split()
                        name, x, y = parts[0], int(parts[1]), int(parts[2])
                        options = " ".join(parts[3:]) if len(parts) > 3 else ""
                        map_data["hubs"].append(
                            {"name": name, "x": x, "y": y, "options": options}
                        )
                    elif line.startswith("connection:"):
                        connection = line.split(":")[1].strip()

                        # Handle metadata
                        parts = connection.split("[", 1)
                        conn_names = parts[0].strip()
                        metadata = "[" + parts[1] if len(parts) > 1 else ""

                        if "-" in conn_names:
                            src, dst = conn_names.split("-", 1)
                            map_data["connections"].append(
                                {
                                    "src": src.strip(),
                                    "dst": dst.strip(),
                                    "options": metadata,
                                }
                            )
        except Exception as e:
            print(f"Error reading file {filepath}: {e}", file=sys.stderr)
            sys.exit(1)

        return map_data

    def select_and_parse_map(self) -> Optional[Dict[str, Any]]:
        """
        Interactively select a map file and parse it.

        Returns:
            Optional[Dict[str, Any]]: The parsed map data, or None.
        """
        map_files = self.list_map_files()

        if not map_files:
            print(f"No .txt files found in '{self.maps_dir}' directory.")
            return None

        print("Available maps:")
        for i, file_path in enumerate(map_files):
            print(f"[{i}] {file_path}")

        try:
            choice = input(f"Select a map (0-{len(map_files) - 1}): ")
            index = int(choice)
            if 0 <= index < len(map_files):
                selected_file = map_files[index]
                print(f"\nParsing: {selected_file}")
                return self.parse_map_file(selected_file)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        return None
