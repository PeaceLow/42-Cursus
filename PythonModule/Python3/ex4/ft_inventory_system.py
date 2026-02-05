#!/usr/bin/env python3

import sys


def to_int(s: str) -> int:
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    res = 0
    for c in s:
        if c in digits:
            res = res * 10 + digits[c]
    return res


def main() -> None:
    inventory = dict()

    # Parsing arguments
    for arg in sys.argv[1:]:
        key = ""
        val = ""
        is_val = False
        for c in arg:
            if c == ':' and not is_val:
                is_val = True
                continue
            if is_val:
                if not ('0' <= c <= '9'):
                    raise ValueError(f"Invalid quantity '{c}' "
                                     f"in argument '{arg}'")
                val += c
            else:
                key += c

        if not is_val:
            raise ValueError(f"Missing ':' in argument '{arg}'")
        if not key:
            raise ValueError(f"Missing name in argument '{arg}'")
        if not val:
            raise ValueError(f"Missing quantity in argument '{arg}'")
        inventory.update({key: to_int(val)})

    # Calculations
    total = 0
    for qty in inventory.values():
        total += qty

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")
    print("")

    # Sorting
    # Conversion en liste de tuples pour trier par quantité
    items = [(k, v) for k, v in inventory.items()]
    size = len(items)
    i = 0
    while i < size:
        j = 0
        while j < size - i - 1:
            # Sort by quantity (index 1) descending
            if items[j][1] < items[j + 1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]
            j += 1
        i += 1

    print("=== Current Inventory ===")
    for name, qty in items:
        pct = (qty / total * 100) if total else 0.0
        unit = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit} ({pct:.1f}%)")
    print("")

    print("=== Inventory Statistics ===")
    if items:
        # Unpacking tuples for most/least abundant
        m_name, m_qty = items[0]
        l_name, l_qty = items[-1]
        m_unit = "unit" if m_qty == 1 else "units"
        l_unit = "unit" if l_qty == 1 else "units"
        print(f"Most abundant: {m_name} ({m_qty} {m_unit})")
        print(f"Least abundant: {l_name} ({l_qty} {l_unit})")
    print("")

    # Categories using nested dictionaries
    categories = dict()
    categories["Moderate"] = dict()
    categories["Scarce"] = dict()

    for name, qty in inventory.items():
        if qty > 3:
            categories["Moderate"].update({name: qty})
        else:
            categories["Scarce"].update({name: qty})

    print("=== Item Categories ===")
    print(f"Moderate: {categories.get('Moderate')}")
    print(f"Scarce: {categories.get('Scarce')}")
    print("")

    # Suggestions
    print("=== Management Suggestions ===")
    restock = [name for name, qty in inventory.items() if qty < 2]
    print(f"Restock needed: {restock}")
    print("")

    # Dictionary Properties Demo
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {[k for k in inventory.keys()]}")
    print(f"Dictionary values: {[v for v in inventory.values()]}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    main()
