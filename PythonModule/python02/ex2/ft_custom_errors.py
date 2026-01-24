class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Not enough water in the Tank!"""
    pass


def test_custom_errors():
    """
    Demonstrates the use of custom exceptions in a garden monitoring system.
    """
    print("=== Garden Custom Errors Demo ===\n")

    # Test PlantError
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    # Test WaterError
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the Tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom errors tested successfully!")


if __name__ == "__main__":
    test_custom_errors()
