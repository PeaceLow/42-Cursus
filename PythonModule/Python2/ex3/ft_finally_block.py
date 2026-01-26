#!/usr/bin/env python3

def water_plants(plant_list):
    """
    Simulate a watering system that processes a list of plants.

    This function demonstrates the use of try-except-finally blocks
    to ensure resources are cleaned up regardless of errors.

    Args:
        plant_list (list): A list of plant names (strings).
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise TypeError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """
    Test the water_plants function with valid and invalid inputs.

    Demonstrates:
    - Normal operation
    - Error handling
    - Finally block execution (cleanup)
    """
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
