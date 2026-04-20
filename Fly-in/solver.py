import heapq
from typing import Dict, List, Tuple, Optional
from graph import Graph, Zone, Connection


class ReservationTable:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.zones: Dict[str, Dict[int, int]] = {
            name: {} for name in graph.zones}
        self.conns: Dict[Connection, Dict[int, int]] = {
            c: {} for c in graph.connections}

    def can_occupy_zone(self, zone_name: str, turn: int) -> bool:
        start_name = self.graph.start_zone.name \
            if self.graph.start_zone else ""
        end_name = self.graph.end_zone.name if self.graph.end_zone else ""

        if zone_name == start_name or zone_name == end_name:
            return True
        z = self.graph.zones[zone_name]
        return self.zones[zone_name].get(turn, 0) < z.max_drones

    def can_use_conn(self, conn: Connection, turn: int) -> bool:
        return self.conns[conn].get(turn, 0) < conn.max_link_capacity

    def reserve_zone(self, zone_name: str, turn: int) -> None:
        self.zones[zone_name][turn] = self.zones[zone_name].get(turn, 0) + 1

    def reserve_conn(self, conn: Connection, turn: int) -> None:
        self.conns[conn][turn] = self.conns[conn].get(turn, 0) + 1


def get_adjacency_map(
        graph: Graph) -> Dict[str, List[Tuple[Zone, Connection]]]:
    adj: Dict[str, List[Tuple[Zone, Connection]]] = {
        name: [] for name in graph.zones}
    for conn in graph.connections:
        z1, z2 = conn.zone1, conn.zone2
        adj[z1.name].append((z2, conn))
        adj[z2.name].append((z1, conn))
    return adj


def get_zone_cost(zone: Zone) -> float:
    if zone.zone_type == "blocked":
        return float('inf')
    elif zone.zone_type == "restricted":
        return 2.0
    elif zone.zone_type == "priority":
        return 0.999
    return 1.0


def find_time_space_path(
        graph: Graph,
        rt: ReservationTable,
        start: Zone,
        end: Zone) -> List[Tuple[int, str]]:
    adj = get_adjacency_map(graph)

    # Priority queue: (cost, turn, zone_name)
    pq: List[Tuple[float, int, str]] = [(0.0, 0, start.name)]

    # Keep track of minimum cost to reach (turn, zone_name)
    min_cost: Dict[Tuple[int, str], float] = {(0, start.name): 0.0}

    # came_from[(turn, zone_name)] = (prev_turn, prev_zone_name, action, conn)
    came_from: Dict[Tuple[int, str],
                    Tuple[int, str, str, Optional[Connection]]] = {}

    best_end_turn = float('inf')
    best_end_state = None

    while pq:
        cost, t, u = heapq.heappop(pq)

        if u == end.name:
            if t < best_end_turn:
                best_end_turn = t
                best_end_state = (t, u)
            break

        if cost > min_cost.get((t, u), float('inf')):
            continue

        if t > 2000:
            continue

        # 1. WAIT action
        if rt.can_occupy_zone(u, t + 1):
            nxt_cost = cost + 1.0
            if nxt_cost < min_cost.get((t + 1, u), float('inf')):
                min_cost[(t + 1, u)] = nxt_cost
                came_from[(t + 1, u)] = (t, u, 'WAIT', None)
                heapq.heappush(pq, (nxt_cost, t + 1, u))

        # 2. MOVE actions
        for v, conn in adj[u]:
            if v.zone_type == "blocked":
                continue

            z_cost = get_zone_cost(v)

            if z_cost == 1.0 or z_cost == 0.999:
                if rt.can_use_conn(
                        conn,
                        t + 1) and rt.can_occupy_zone(v.name, t + 1):
                    nxt_cost = cost + z_cost
                    if nxt_cost < min_cost.get((t + 1, v.name), float('inf')):
                        min_cost[(t + 1, v.name)] = nxt_cost
                        came_from[(t + 1, v.name)] = (t, u, 'MOVE1', conn)
                        heapq.heappush(pq, (nxt_cost, t + 1, v.name))

            elif z_cost == 2.0:
                if rt.can_use_conn(
                        conn,
                        t + 1) and rt.can_occupy_zone(v.name, t + 2):
                    nxt_cost = cost + z_cost
                    if nxt_cost < min_cost.get((t + 2, v.name), float('inf')):
                        min_cost[(t + 2, v.name)] = nxt_cost
                        came_from[(t + 2, v.name)] = (t, u, 'MOVE2', conn)
                        heapq.heappush(pq, (nxt_cost, t + 2, v.name))

    if not best_end_state:
        return []

    # Reconstruct path backwards
    path = []
    curr: Tuple[int, str] = best_end_state
    while curr[0] != 0 or curr[1] != start.name:
        prev_t, prev_u, act, connection = came_from[curr]
        path.append((prev_t, prev_u, act, connection, curr[1]))
        curr = (prev_t, prev_u)

    path.reverse()

    # Apply reservations and build instructions
    instructions: List[Tuple[int, str]] = []
    for prev_t, prev_u, act, conn_used, target in path:
        if act == 'WAIT':
            rt.reserve_zone(prev_u, prev_t + 1)
        elif act == 'MOVE1' and conn_used:
            rt.reserve_conn(conn_used, prev_t + 1)
            rt.reserve_zone(target, prev_t + 1)
            instructions.append((prev_t + 1, target))
        elif act == 'MOVE2' and conn_used:
            rt.reserve_conn(conn_used, prev_t + 1)
            rt.reserve_zone(target, prev_t + 2)
            conn_name = f"{conn_used.zone1.name}-{conn_used.zone2.name}"
            instructions.append((prev_t + 1, conn_name))
            instructions.append((prev_t + 2, target))

    return instructions


def compute_all_paths(graph: Graph) -> Dict[int, List[Tuple[int, str]]]:
    rt = ReservationTable(graph)
    all_instructions: Dict[int, List[Tuple[int, str]]] = {}

    if not graph.start_zone or not graph.end_zone:
        return all_instructions

    for drone_id in range(1, graph.nb_drones + 1):
        inst = find_time_space_path(
            graph, rt, graph.start_zone, graph.end_zone)
        if inst:
            all_instructions[drone_id] = inst

    return all_instructions
