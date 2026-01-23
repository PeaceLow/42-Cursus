#!/usr/bin/env python3

"""
This module demonstrates a factory-like creation of multiple Plant objects.
It processes a list of data to instantiate objects.
"""


class Plant:
    """
    Represents a plant entity created by the factory.
    """

    def __init__(self, name, height, age):
        """
        Initialize the plant.

        Args:
            name (str): The name of the plant.
            height (int): The current height.
            age (int): The current age.
        """
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    plants = []
    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")

    print(f"Total plants created: {len(plants)}")
