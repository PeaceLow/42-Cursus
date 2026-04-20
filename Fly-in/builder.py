from typing import Dict, Any
from graph import Graph


def parse_metadata(metadata_str: str) -> Dict[str, str]:
    """
    Parses options metadata string like
    "[zone=restricted color=red max_drones=2]"
    into a dictionary
    {"zone": "restricted", "color": "red", "max_drones": "2"}.
    """
    metadata_str = metadata_str.strip()
    if not metadata_str:
        return {}

    if metadata_str.startswith("[") and metadata_str.endswith("]"):
        metadata_str = metadata_str[1:-1]

    result = {}
    for token in metadata_str.split():
        if "=" in token:
            key, val = token.split("=", 1)
            result[key] = val
    return result


def build_graph(map_data: Dict[str, Any]) -> Graph:
    """
    Constructs a Graph objects from the dictionary mapped by MapParser.
    """
    graph = Graph()
    graph.nb_drones = map_data.get("nb_drones", 0)

    # Process hubs
    all_hubs = []
    if map_data.get("start_hub"):
        all_hubs.append((map_data["start_hub"], "start"))
    if map_data.get("end_hub"):
        all_hubs.append((map_data["end_hub"], "end"))

    for hub in map_data.get("hubs", []):
        all_hubs.append((hub, "normal"))

    for hub_data, role in all_hubs:
        meta = parse_metadata(hub_data.get("options", ""))

        zone_type = meta.get("zone", "normal")
        color = meta.get("color", None)
        max_drones = int(meta.get("max_drones", 1))

        name = hub_data["name"]
        x = hub_data["x"]
        y = hub_data["y"]

        zone = graph.add_zone(name, x, y, zone_type, color, max_drones)

        if role == "start":
            graph.start_zone = zone
        elif role == "end":
            graph.end_zone = zone

    # Process connections
    for conn_data in map_data.get("connections", []):
        meta = parse_metadata(conn_data.get("options", ""))
        max_cap = int(meta.get("max_link_capacity", 1))

        src = conn_data["src"]
        dst = conn_data["dst"]

        graph.add_connection(src, dst, max_cap)

    return graph
