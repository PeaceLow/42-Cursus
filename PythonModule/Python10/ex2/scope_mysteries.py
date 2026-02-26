import typing


def mage_counter() -> typing.Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> typing.Callable[[int], int]:
    current_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal current_power
        try:
            current_power += power_to_add
        except TypeError:
            print("Error: Power to add must be a number.")
        return current_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> typing.Callable[[str], str]:
    def apply_enchantment(item_name: str) -> str:
        try:
            return f"{enchantment_type} {item_name}"
        except Exception:
            # Fallback for unexpected types
            return f"{enchantment_type} {str(item_name)}"

    return apply_enchantment


def memory_vault() -> typing.Dict[str, typing.Callable]:
    memory_storage: typing.Dict[typing.Any, typing.Any] = {}

    def store(key: typing.Any, value: typing.Any) -> None:
        try:
            memory_storage[key] = value
        except TypeError:
            print("Error: Key must be hashable.")

    def recall(key: typing.Any) -> typing.Any:
        return memory_storage.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main():
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print()

    print("Testing enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")

    print(fire_enchant("Sword"))
    print(ice_enchant("Shield"))
    print()

    print("Testing spell accumulator...")
    acc = spell_accumulator(10)
    print(f"Initial 10, add 5: {acc(5)}")
    print(f"Add 20: {acc(20)}")
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']("secret_spell", "Fireball")
    print(f"Recall secret_spell: {vault['recall']('secret_spell')}")
    print(f"Recall unknown: {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
