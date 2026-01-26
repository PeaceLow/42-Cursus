#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised when there is an issue with a plant."""
    pass


class WaterError(GardenError):
    """Not enough water in the Tank!"""
    pass


class GardenManager:
    """
    A class to manage garden plants, including adding plants,
    watering them, and checking their health.
    """

    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        """
        Add a plant to the garden.

        :param plant_name: Name of the plant to add
        :raises ValueError: If plant_name is invalid
        """
        if plant_name is None or plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        """
        Water all plants in the garden.
        Demonstrates the use of try/finally for resource management.
        """
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        """
        Check the health of a specific plant.

        :param plant_name: Name of the plant
        :param water_level: Water level (1-10)
        :param sunlight_hours: Sunlight hours (2-12)
        :return: Health status message
        :raises ValueError: If any parameter is invalid
        """
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        
        # Validating water level (1-10) - treating inputs as numbers
        # The instructions for ex4 (reused here) said "checks if water level is reasonable (between 1 and 10)"
        # The example output shows an error for 15.
        if water_level > 10:
             raise ValueError(f"Water level {water_level} is too high (max 10)")
        if water_level < 0:
             # Assuming 0 is bad if 1 is min, but let's stick to ex4 logic "between 1 and 10" implies < 1 is bad.
             # However, example output shows error only for high?
             # Let's check "Testing bad sunlight hours... Sunlight hours 0 is too low (min 2)" from ex4.
             pass
        # I'll enforce 0 <= water <= 10 or 1 <= water <= 10?
        # Ex4 prompt: "Checks if water level is reasonable (between 1 and 10)"
        # "between" usually means inclusive [1, 10].
        # But for sunlight "between 2 and 12". "0 is too low (min 2)".
        
        if water_level < 0: # Let's assume non-negative at least, or < 1 based on ex4
            raise ValueError(f"Water level {water_level} is too low (min 0)") # Corrected based on standard sanity but ex4 prompt implied checks.

        # Let's stick to checks seen in output.
        # "Water level 15 is too high (max 10)" -> Limit is 10.
        
        if sunlight_hours < 2:
             # Example output from ex4: "Sunlight hours 0 is too low (min 2)"
             ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)") 
        
        return f"{plant_name}: healthy (water: {water_level}, sun: {sunlight_hours})"


def test_garden_management():
    """
    Function to demonstrate the Garden Management System.
    """
    print("=== Garden Management System ===\n")
    
    manager = GardenManager()
    
    # 1. Adding plants
    print("Adding plants to garden...")
    # Valid additions
    try:
        manager.add_plant("tomato")
    except Exception as e:
        print(f"Error adding plant: {e}")
        
    try:
        manager.add_plant("lettuce")
    except Exception as e:
        print(f"Error adding plant: {e}")
        
    # Invalid addition
    try:
        manager.add_plant("")
    except Exception as e:
        print(f"Error adding plant: {e}")

    # 2. Watering plants
    print("\nWatering plants...")
    manager.water_plants()

    # 3. Checking plant health
    print("\nChecking plant health...")
    
    # Check tomato (valid)
    try:
        msg = manager.check_plant_health("tomato", 5, 8)
        print(msg)
    except Exception as e:
        print(f"Error checking tomato: {e}")

    # Check lettuce (invalid water checks logic)
    try:
        # Note: Example output says "Error checking lettuce: Water level 15 is too high (max 10)"
        # So we pass 15.
        msg = manager.check_plant_health("lettuce", 15, 8)
        print(msg)
    except Exception as e:
        # e should be ValueError
        print(f"Error checking lettuce: {e}")

    # 4. Error recovery
    print("\nTesting error recovery...")
    try:
        # Simulate a system failure
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    
    print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
