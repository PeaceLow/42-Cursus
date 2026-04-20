import argparse
from parsing import MapParser
from builder import build_graph
from simulation import Simulation
from visualizer import MapVisualizer


def main() -> None:
    """
    Main entry point for the simulation program.
    """
    arg_parser = argparse.ArgumentParser(description='Fly-in Drone Simulation')
    arg_parser.add_argument(
        '--visual',
        action='store_true',
        help='Launch graphical visualization of the simulation')
    args = arg_parser.parse_args()

    parser = MapParser()
    data = parser.select_and_parse_map()
    if data:
        graph = build_graph(data)

        print("\\n--- Simulation Initialization ---")
        sim = Simulation(graph)
        sim.run()

        if args.visual:
            print("\\nLaunching Map Visualizer...")
            visualizer = MapVisualizer(sim)
            visualizer.show()


if __name__ == "__main__":
    main()
