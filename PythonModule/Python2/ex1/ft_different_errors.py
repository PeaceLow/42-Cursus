#!/usr/bin/env python3

def garden_operations():
    """
    Demonstrates handling of multiple potential errors
    in a garden monitoring system.
    """
    try:
        int("abc")
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types():
    """
    Shows each type of error happening and catches the error.
    """
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("garden")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0  # type: ignore
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        my_plants = {"rose": "red"}
        print(my_plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    garden_operations()

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
