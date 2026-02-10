from ex2.EliteCard import EliteCard
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")

    card_methods = [
        method for method in dir(Card)
        if callable(getattr(Card, method)) and not method.startswith("__")
    ]
    combatable_methods = [
        method for method in dir(Combatable)
        if callable(getattr(Combatable, method))
        and not method.startswith("__")
    ]
    magical_methods = [
        method for method in dir(Magical)
        if callable(getattr(Magical, method)) and not method.startswith("__")
    ]
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    print("\nPlaying Arcane Warrior (Elite Card):")
    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=7,
        rarity="Legendary",
        attack_power=5,
        defense=3,
        health=8,
        magic_power=4,
        mana_pool=10
    )
    print("\nCombat phase:")
    attack_result = arcane_warrior.attack(target="Enemy Orc")
    print(f"Attack result: {attack_result}")
    defense_result = arcane_warrior.defend(incoming_damage=5)
    print(f"Defense result: {defense_result}")

    print("\nMagic phase:")
    spell_result = arcane_warrior.cast_spell(
        spell_name="Fireball",
        targets=["Enemy Orc", "Enemy Goblin"]
    )
    print(f"Spell cast: {spell_result}")
    mana_channel_result = arcane_warrior.channel_mana(amount=2)
    print(f"Mana channel result: {mana_channel_result}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
