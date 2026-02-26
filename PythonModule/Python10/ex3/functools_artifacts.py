from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    func = ops.get(operation)
    if not func:
        raise ValueError("Opération non supportée. Utilisez 'add', "
                         "'multiply', 'max' ou 'min'.")
    return reduce(func, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantments = {
        'fire_enchant': partial(base_enchantment, power=50, element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
        'lightning_enchant': partial(base_enchantment,
                                     power=50, element='lightning')
    }
    return enchantments


def cast_spell(power: int, element: str, target: str) -> str:
    return f"Sort de {element} lancé sur {target} avec" \
           f" une puissance de {power} !"


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast_spell(spell: Any) -> Any:
        return f"Sort inconnu : {spell} se dissipe dans le vide."

    @cast_spell.register
    def _(spell: int):
        return f"Sort de dégâts ! Inflige {spell} points de vie."

    @cast_spell.register
    def _(spell: str):
        return f"Enchantement lancé : {spell}."

    @cast_spell.register
    def _(spell: list):
        return [cast_spell(s) for s in spell]

    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    number = [40, 30, 20, 10]
    print("Sum:", spell_reducer(number, "add"))
    print("Product:", spell_reducer(number, "multiply"))
    print("Max:", spell_reducer(number, "max"))

    print("\nTesting partial enchanter...")
    grimoire = partial_enchanter(cast_spell)
    print(grimoire['fire_enchant'](target="Gobelin"))
    print(grimoire['ice_enchant'](target="Dragon"))

    print("\nTesting memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    damage_spell = 50
    enchant_spell = "Bouclier d'Ether"
    multi_cast = [10, "Force", 25]
    unknown_spell = 12.5
    print(f"Test Int : {cast(damage_spell)}")
    print(f"Test Str : {cast(enchant_spell)}")
    print(f"Test List : {cast(multi_cast)}")
    print(f"Test Default : {cast(unknown_spell)}")


if __name__ == "__main__":
    main()
