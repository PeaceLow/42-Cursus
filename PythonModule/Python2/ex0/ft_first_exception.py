#!/usr/bin/env python3

def check_temperature(temp_str):
    """
    Takes a string input, converts it to an integer, and validates if it is
    within the safe range for plants (0-40).

    Args:
        temp_str (str): The temperature as a string.

    Returns:
        int: The valid temperature.
        None: If the input is invalid or out of range.
    """
    try:
        temp_int = int(temp_str)
        if 0 <= temp_int <= 40:
            return temp_int
        elif temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)\n")
            return None
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)\n")
            return None
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None


def test_temperature_input():
    """
    Runs a series of tests with predefined inputs to demonstrate
    the robustness of the check_temperature function.
    """
    test_cases = ["25", "abc", "100", "-50"]

    for temp in test_cases:
        print(f"Testing temperature: {temp}")
        result = check_temperature(temp)
        if result is not None:
            print(f"Temperature {result}°C is perfect for plants!\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
