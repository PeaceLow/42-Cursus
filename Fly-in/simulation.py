from typing import List, Dict, Tuple
from graph import Graph
from solver import compute_all_paths


class Simulation:
    """
    Handles the execution of the drone routing simulation.
    """

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.turn: int = 1

        self.instructions: Dict[int, List[Tuple[int, str]]
                                ] = compute_all_paths(graph)
        self.finished = False

    def is_finished(self) -> bool:
        """ Returns True if all drones have completed their schedules. """
        return self.finished

    def run(self) -> None:
        """ Main loop for the simulation. """
        print(f"Starting simulation with {self.graph.nb_drones} drones...")

        if not self.instructions:
            print("No valid paths found. Simulation aborted.")
            return

        max_turn = 0
        for drone_id, sched in self.instructions.items():
            if sched:
                max_turn = max(max_turn, sched[-1][0])

        while self.turn <= max_turn:
            moves_this_turn: List[str] = []

            for drone_id in range(1, self.graph.nb_drones + 1):
                sched = self.instructions.get(drone_id, [])
                for t, target in sched:
                    if t == self.turn:
                        moves_this_turn.append(f"D{drone_id}-{target} ")
                        break

            if moves_this_turn:
                print(" ".join(moves_this_turn))

            self.turn += 1

        self.finished = True
        print(f"Simulation ended in {max_turn} turns.")
