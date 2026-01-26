#!/usr/bin/env python3

import sys
import math


def ft_coordinate_system(args) -> None:
    """
    Convertit des coordonnées cartésiennes en coordonnées polaires
    ou vice versa, selon les arguments fournis en ligne de commande.

    :param args: Liste des arguments de la ligne de commande
    :return: None
    """
    if len(args) != 2:
        print("Usage: ft_coordinate_system.py <x,y,z>")
        return

    x1, y1, z1 = (0, 0, 0)

    try:
        parts = args[1].split(',')
        if len(parts) != 3:
            raise ValueError
        x2 = int(parts[0])
        y2 = int(parts[1])
        z2 = int(parts[2])
        print(f"Parsing coordinates: \"{args[1]}\"")
    except ValueError:
        print("Invalid coordinates provided.")
        return

    if len(args) == 2:
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        print(f"Distance between ({x1}, {y1}, {z1})"
              f" and ({x2}, {y2}, {z2}): {dist:.2f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system(sys.argv)
