from typing import Callable, Any, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args: Any, **kwargs: Any) -> tuple:
        try:
            result1 = spell1(*args, **kwargs)
            result2 = spell2(*args, **kwargs)
            return (result1, result2)
        except Exception as e:
            print(f"Error in spell_combiner: {e}")
            return tuple()
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(*args: Any, **kwargs: Any) -> Any:
        try:
            result = base_spell(*args, **kwargs)
            return result * multiplier
        except Exception as e:
            print(f"Error in power_amplifier: {e}")
            return None
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_spell(*args: Any, **kwargs: Any) -> Any:
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        except Exception as e:
            print(f"Error in conditional_caster: {e}")
            return "Spell fizzled"
    return cast_spell


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence_spell(*args: Any, **kwargs: Any) -> List[Any]:
        results = []
        try:
            for spell in spells:
                results.append(spell(*args, **kwargs))
            return results
        except Exception as e:
            print(f"Error in spell_sequence: {e}")
            return results
    return sequence_spell


if __name__ == "__main__":
    # Testing spell combiner
    print("Testing spell combiner...")

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    combined = spell_combiner(fireball, heal)
    res = combined("Dragon")
    print(f"Combined spell result: {res[0]}, {res[1]}")
    print("")

    # Testing power amplifier
    print("Testing power amplifier...")

    def damage_spell() -> int:
        return 10

    mega_fireball = power_amplifier(damage_spell, 3)
    original = damage_spell()
    amplified = mega_fireball()
    print(f"Original: {original}, Amplified: {amplified}")
