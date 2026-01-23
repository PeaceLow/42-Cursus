#!/usr/bin/env python3

"""
This module defines the Plant class for the garden registry.
It handles basic plant data storage and display.
"""


class Plant:
    """
    Represents a plant with basic attributes.
    """

    def __init__(self, name, height, age):
        """
        Initialize a new plant instance.

        Args:
            name (str): The name of the plant.
            height (int): The height of the plant in cm.
            age (int): The age of the plant in days.
        """
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        """
        Print the details of the plant to the console.
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    rose.display()
    sunflower.display()
    cactus.display()
