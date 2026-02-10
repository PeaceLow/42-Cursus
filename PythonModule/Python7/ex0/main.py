from .CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    firedragon = CreatureCard(name="Fire Dragon", cost=5, rarity='Legendary',
                              attack=7, health=5)
    print(firedragon.get_card_info())

    print("Playing Fire Dragon with 6 mana available:")
    if firedragon.is_playable(available_mana=6):
        print("Playable: True")
        print(f"Play Result: "
              f"{firedragon.play(game_state={'player_health': 30})}")
    else:
        print("Playable: False")

    print("\nFire Dragon attacks Goblin Warrior:")
    attack_result = firedragon.attack_target(target="Goblin Warrior")
    print(f"Attack Result: {attack_result}")

    print("\nTesting insufficient mana (3 available):")
    if firedragon.is_playable(available_mana=3):
        print("Playable: True")
    else:
        print("Playable: False")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
