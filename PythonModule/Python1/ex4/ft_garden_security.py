#!/usr/bin/env python3

"""
This module implements a SecurePlant class with encapsulation.
It ensures that plant properties like height
and age cannot be set to invalid values.
"""


class SecurePlant:
    """
    A plant class with secure attribute management.
    """

    def __init__(self, name, age, height):
        """
        Initialize the secure plant.

        Args:
            name (str): The name of the plant.
            age (int): The initial age.
            height (int): The initial height.
        """
        self.name = name
        self.__age = 0
        self.__height = 0
        self.set_age(age)
        self.set_height(height)

    def set_height(self, height):
        """
        Set the height of the plant securely.

        Args:
            height (int): The new height value. Must be non-negative.
        """
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = height

    def get_height(self):
        """
        Get the current height.

        Returns:
            int: The height of the plant.
        """
        return self.__height

    def set_age(self, age):
        """
        Set the age of the plant securely.

        Args:
            age (int): The new age value. Must be non-negative.
        """
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = age

    def get_age(self):
        """
        Get the current age.

        Returns:
            int: The age of the plant.
        """
        return self.__age


if __name__ == '__main__':
    print("=== Garden Security System ===")
    rose = SecurePlant('Rose', 30, 25)
    print(f"Plant created: {rose.name}")
    print(f"Height updated: {rose.get_height()}cm [OK]")
    print(f"Age updated: {rose.get_age()} days [OK]\n")
    rose.set_height(-5)
    print(f"\nCurrent plant: {rose.name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")
