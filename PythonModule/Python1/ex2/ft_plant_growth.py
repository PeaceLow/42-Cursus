#!/usr/bin/env python3

"""
This module simulates the growth of a plant over time.
It demonstrates modifying object attributes.
"""


class Plant:
    """
    Represents a plant that can grow over time.
    """

    def __init__(self, name, height, age):
        """
        Initialize the plant with its characteristics.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant.
            age (int): The age of the plant.
        """
        self.name = name
        self.height = height
        self.a = age

    def get_info(self):
        """
        Display the current information about the plant.
        """
        print(f"{self.name}: {self.height}cm, {self.a} days old")

    def grow(self):
        """
        Simulate the plant growing by increasing height.
        """
        self.height += 1

    def age(self):
        """
        Simulate the plant growing by increasing age.
        """
        self.a += 1


if __name__ == "__main__":
    print("=== Day 1 ===")
    plant = Plant("Rose", 25, 30)
    plant.get_info()

    # Simulate growth over 6 days (Day 1 to 7)
    for _ in range(6):
        plant.grow()
        plant.age()

    print("=== Day 7 ===")
    plant.get_info()
    print("Growth this week: +6cm")
