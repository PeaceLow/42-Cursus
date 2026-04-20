from typing import List, Dict, Optional


class Zone:
    """
    Represents a zone/node in the drone network.
    """

    def __init__(self, name: str, x: int, y: int, zone_type: str = "normal",
                 color: Optional[str] = None, max_drones: int = 1) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.color = color
        self.max_drones = max_drones
        self.current_drones = 0

    def __repr__(self) -> str:
        return f"Zone({
            self.name}, type={
            self.zone_type}, capacity={
            self.max_drones})"


class Connection:
    """
    Represents a connection/edge between two zones.
    """

    def __init__(
            self,
            zone1: Zone,
            zone2: Zone,
            max_link_capacity: int = 1) -> None:
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity

    def get_other_zone(self, zone: Zone) -> Zone:
        if zone == self.zone1:
            return self.zone2
        return self.zone1

    def __repr__(self) -> str:
        return f"Connection({
            self.zone1.name}-{
            self.zone2.name}, capacity={
            self.max_link_capacity})"


class Graph:
    """
    Represents the complete network of zones and connections.
    """

    def __init__(self) -> None:
        self.zones: Dict[str, Zone] = {}
        self.connections: List[Connection] = []
        self.start_zone: Optional[Zone] = None
        self.end_zone: Optional[Zone] = None
        self.nb_drones: int = 0

    def add_zone(self, name: str, x: int, y: int, zone_type: str = "normal",
                 color: Optional[str] = None, max_drones: int = 1) -> Zone:
        """Adds a new zone to the graph."""
        zone = Zone(name, x, y, zone_type, color, max_drones)
        self.zones[name] = zone
        return zone

    def add_connection(
            self,
            name1: str,
            name2: str,
            max_link_capacity: int = 1) -> None:
        """Adds a bidirectional connection between two existing zones."""
        if name1 in self.zones and name2 in self.zones:
            conn = Connection(
                self.zones[name1],
                self.zones[name2],
                max_link_capacity)
            self.connections.append(conn)

    def print_info(self) -> None:
        """Prints graph information."""
        print(f"Graph initialized with {len(self.zones)} zones "
              f"and {len(self.connections)} connections.")
        if self.start_zone and self.end_zone:
            print(f"Start: {self.start_zone.name} | End: {self.end_zone.name}")
        print(f"Total Drones: {self.nb_drones}")
