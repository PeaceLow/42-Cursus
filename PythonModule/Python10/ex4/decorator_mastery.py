import time
import functools
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Spell completed in {execution_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # Check for 'power' in kwargs
            power = kwargs.get('power')
            if power is None:
                found_power = None
                for arg in args:
                    if isinstance(arg, int):
                        found_power = arg
                        break

                if found_power is not None:
                    power = found_power
                else:
                    return "Insufficient power for this spell"

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        # replace spaces to check for isalpha
        return name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main():
    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print(fireball())
    mage = MageGuild()

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Raistlin Majere"))
    print(MageGuild.validate_mage_name("X"))

    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Spark", 5))

    print("\nTesting retry_spell...")

    @retry_spell(max_attempts=3)
    def broken_spell():
        raise ValueError("Fizzle")

    print(broken_spell())


if __name__ == "__main__":
    main()
