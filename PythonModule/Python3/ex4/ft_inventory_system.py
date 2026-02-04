#!/usr/bin/env python3

import sys


def to_int(s: str) -> int:
    digit_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    num = 0
    for char in s:
        if char in digit_map:
            num = num * 10 + digit_map[char]
    return num


def main() -> None:
    inventory = dict()

    # Verification des arguments
    args = sys.argv[1:]

    for arg in args:
        # Parsing item:quantity
        colon_index = -1
        idx = 0
        for char in arg:
            if char == ':':
                colon_index = idx
            idx += 1

        if colon_index != -1:
            name = arg[:colon_index]
            quantity_str = arg[colon_index + 1:]
            # Custom to_int function
            quantity = to_int(quantity_str)
            inventory[name] = quantity

    # Calculations
    total_items = 0
    for qty in inventory.values():
        total_items += qty

    unique_items = len(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}")
    print("")

    # Sort items by quantity descending
    # Create list of tuples manually
    item_list = [(k, v) for k, v in inventory.items()]

    # Bubble sort
    n = len(item_list)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            # Compare quantities (index 1), descending order
            if item_list[j][1] < item_list[j + 1][1]:
                # Swap
                pair_one = item_list[j]
                pair_two = item_list[j + 1]
                item_list[j] = pair_two
                item_list[j + 1] = pair_one
            j += 1
        i += 1

    print("=== Current Inventory ===")
    for name, qty in item_list:
        # Division is an operator, allowed.
        percent = (qty / total_items) * 100 if total_items > 0 else 0.0

        unit_str = "unit"
        if qty != 1:
            unit_str = "units"

        print(f"{name}: {qty} {unit_str} ({percent:.1f}%)")
    print("")

    # Statistics
    print("=== Inventory Statistics ===")
    if item_list:
        most_name, most_qty = item_list[0]
        least_name, least_qty = item_list[-1]

        most_unit = "unit" if most_qty == 1 else "units"
        least_unit = "unit" if least_qty == 1 else "units"

        print(f"Most abundant: {most_name} ({most_qty} {most_unit})")
        print(f"Least abundant: {least_name} ({least_qty} {least_unit})")
    print("")

    # Categories
    categories = dict()
    categories["Moderate"] = dict()
    categories["Scarce"] = dict()

    for name, qty in inventory.items():
        # Threshold > 3 for Moderate (Potion:5 is Moderate, Armor:3 is Scarce)
        if qty > 3:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    print("=== Item Categories ===")
    # Using .get() as authorized
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")
    print("")

    # Suggestions
    # Threshold < 2 (Sword:1, Helmet:1 are Restock. Shield:2 is not)
    restock = [name for name, qty in inventory.items() if qty < 2]

    print("=== Management Suggestions ===")
    print(f"Restock needed: {restock}")
    print("")

    # Demo
    print("=== Dictionary Properties Demo ===")
    # Format list output directly
    # Using list comprehension to create lists
    keys_list = [k for k in inventory.keys()]
    values_list = [v for v in inventory.values()]
    print(f"Dictionary keys: {keys_list}")
    print(f"Dictionary values: {values_list}")

    has_sword = 'sword' in inventory
    # Need to convert boolean to string explicitly? f-string does it.
    print(f"Sample lookup - 'sword' in inventory: {has_sword}")


if __name__ == "__main__":
    main()
