from typing import Optional, List, Tuple
from graph import Zone, Connection


class Drone:
    """
    Represents a single drone in the simulation.
    """

    def __init__(self, drone_id: int, start_zone: Zone) -> None:
        """
        Initialize the drone with an ID and starting zone.
        """
        self.drone_id: int = drone_id
        self.current_zone: Optional[Zone] = start_zone
        self.current_connection: Optional[Connection] = None

        self.path: List[Tuple[Zone, Connection]] = []
        self.path_index: int = 0

        self.transit_time: int = 0
        self.has_finished: bool = False

    @property
    def name(self) -> str:
        """
        Returns the formatted name of the drone (e.g., D1).
        """
        return f"D{self.drone_id}"

    def __repr__(self) -> str:
        res = f"Drone({self.name}, finished={self.has_finished})"
        return res
