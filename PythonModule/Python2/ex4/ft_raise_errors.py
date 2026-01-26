#!/usr/bin/env python3

def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Docstring for check_plant_health

    Check if the plant name is valid and if the water level
    and sunlight hours are within acceptable ranges.

    :param plant_name: Name of the plant to check
    :param water_level: Level of water the plant has received
    :param sunlight_hours: Number of hours the plant
    has been exposed to sunlight

    :return: A success message if the plant is healthy
    :raises ValueError: If plant_name is invalid, water_level is out of range,
    or sunlight_hours is out of range
    """
    if plant_name is None or plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    """
    Test the check_plant_health function with various inputs.

    Demonstrates:
    - Valid plant health checks
    - Error handling for invalid inputs
    """
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 6))      # valid values
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 6)          # empty plant name
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("Tulip", 15, 6)    # high water level
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Sunflower", 5, 0)  # 0 sunlight hours
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("\nAll error raising tests completed!")
