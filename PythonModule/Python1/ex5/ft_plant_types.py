#!/usr/bin/env python3

"""
This module defines a hierarchy of plant types using inheritance.
It includes specific classes for Flowers, Trees, and Vegetables.
"""


class Plant:
    """
    Base class for all plants.
    """

    def __init__(self, name, age, height):
        """
        Initialize the base plant attributes.

        Args:
            name (str): The name of the plant.
            age (int): The age of the plant.
            height (int): The height of the plant.
        """
        self.name = name
        self.age = age
        self.height = height


class Flower(Plant):
    """
    Represents a flower, inheriting from Plant.
    """

    def __init__(self, name, age, height, color):
        """
        Initialize a flower.

        Args:
            name (str): The name of the flower.
            age (int): The age.
            height (int): The height.
            color (str): The color of the flower.
        """
        super().__init__(name=name, age=age, height=height)
        self.color = color

    def bloom(self):
        """
        Simulate the blooming of the flower.
        """
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    """
    Represents a tree, inheriting from Plant.
    """

    def __init__(self, name, age, height, trunk_diameter):
        """
        Initialize a tree.

        Args:
            name (str): The name of the tree.
            age (int): The age.
            height (int): The height.
            trunk_diameter (int): The diameter of the trunk.
        """
        super().__init__(name=name, age=age, height=height)
        self.trunk_diameter = trunk_diameter

    def product_shade(self):
        """
        Simulate the tree producing shade.
        """
        print(f"{self.name} provides 78 square meters of shade\n")


class Vegetable(Plant):
    """
    Represents a vegetable, inheriting from Plant.
    """

    def __init__(self, name, age, height, harvest_season):
        """
        Initialize a vegetable.

        Args:
            name (str): The name of the vegetable.
            age (int): The age.
            height (int): The height.
            harvest_season (str): The season for harvest.
        """
        super().__init__(name=name, age=age, height=height)
        self.harvest_season = harvest_season

    def nutritional_value(self):
        """
        Display information about the nutritional value.
        """
        print(f"{self.name} is rich in vitamin C\n")


if __name__ == '__main__':
    rose = Flower('Rose', 30, 25, 'red')
    tulip = Flower('Tulip', 15, 12, 'blue')

    oak = Tree('Oak', 1825, 500, 50)
    pine = Tree('Pine', 40, 300, 40)

    tomato = Vegetable('Tomato', 90, 80, 'summer')
    carrot = Vegetable('Carrot', 20, 15, 'summer')

    print("=== Garden Plant Types ===\n")
    print(f"{rose.name} (Flower): {rose.height}cm, "
          f"{rose.age} days, {rose.color} color")
    rose.bloom()
    print(f"{tulip.name} (Flower): {tulip.height}cm, "
          f"{tulip.age} days, {tulip.color} color")
    tulip.bloom()

    print(f"{oak.name} (Flower): {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    oak.product_shade()
    print(f"{pine.name} (Flower): {pine.height}cm, {pine.age} days, "
          f"{pine.trunk_diameter}cm diameter")
    pine.product_shade()

    print(f"{tomato.name} (Flower): {tomato.height}cm, {tomato.age} days, "
          f"{tomato.harvest_season} harvest")
    tomato.nutritional_value()
    print(f"{carrot.name} (Flower): {carrot.height}cm, {carrot.age} days, "
          f"{carrot.harvest_season} harvest")
    carrot.nutritional_value()
