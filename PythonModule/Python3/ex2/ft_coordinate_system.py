#!/usr/bin/env python3

import math


def calculate_distance(p1: tuple[int, int, int],
                       p2: tuple[int, int, int]) -> float:
    """
    Calcule la distance euclidienne entre deux points 3D.

    :param p1: Tuple représentant les coordonnées (x1, y1, z1) du premier point
    :param p2: Tuple représentant les coordonnées (x2, y2, z2) du second point
    :return: Distance euclidienne entre les deux points
    """
    return math.sqrt((p2[0] - p1[0])**2 +
                     (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


def main() -> None:
    """
    Fonction principale pour démontrer la gestion des coordonnées.

    :return: None
    """
    print("=== Game Coordinate System ===")
    print()

    # Création des positions et calcul de la distance
    pos1 = (10, 20, 5)
    origin = (0, 0, 0)
    print(f"Position created: {pos1}")
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}")
    print()

    # Parsing coordinates
    coord_str = "3,4,0"
    print(f"Parsing coordinates: \"{coord_str}\"")

    pos2 = None
    try:
        parts = coord_str.split(',')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        pos2 = (x, y, z)
        print(f"Parsed position: {pos2}")
        dist2 = calculate_distance(origin, pos2)
        print(f"Distance between {origin} and {pos2}: {dist2:.1f}")
    except Exception as e:
        print(f"Error parsing coordinates: {e}")

    print()

    # Parsing invalid coordinates
    bad_coord_str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{bad_coord_str}\"")
    try:
        parts = bad_coord_str.split(',')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {e.__class__.__name__}, Args: {e.args}")
    except Exception as e:
        print(f"Error: {e}")

    print()

    # Unpacking demonstration
    print("Unpacking demonstration:")
    if pos2:
        x, y, z = pos2
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
