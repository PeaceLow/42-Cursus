import alchemy


def main() -> None:
    print("\n=== Sacred Scroll Mastery ===\n")
    print("Testing direct module access:")
    fire = alchemy.elements.create_fire()
    water = alchemy.elements.create_water()
    earth = alchemy.elements.create_earth()
    air = alchemy.elements.create_air()
    print(f"alchemy.elements.create_fire(): {fire}")
    print(f"alchemy.elements.create_water(): {water}")
    print(f"alchemy.elements.create_earth(): {earth}")
    print(f"alchemy.elements.create_air(): {air}\n")

    print("Testing package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError:
        print("create_fire() is not accessible")
    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError:
        print("create_water() is not accessible")
    try:
        print(f"alchemy.create_earth(): "
              f"{alchemy.create_earth()}")  # type: ignore
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        print(f"alchemy.create_air(): "
              f"{alchemy.create_air()}")  # type: ignore
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}\n")


if __name__ == "__main__":
    main()
