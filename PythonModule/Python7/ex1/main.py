from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")

    deck = Deck()

    # Creation des cartes
    lightning_bolt = SpellCard("Lightning Bolt", 3, "Common",
                               "Deal 3 damage to target")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Common", 10,
                                "Permanent: +1 mana per turn")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Rare", 4, 4)

    # Ajout au deck
    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    # Stats
    stats = deck.get_deck_stats()
    print(f"Deck stats: {stats}")
    print()

    print("Drawing and playing cards:")
    print()

    # Play cards
    card_types = {
        "SpellCard": "Spell",
        "ArtifactCard": "Artifact",
        "CreatureCard": "Creature"
    }

    # Helper function to get type
    def get_type_str(card):
        return card_types.get(card.__class__.__name__, "Card")

    # Manual Draw to match order of output or just loop
    # The output order: Lightning Bolt, Mana Crystal, Fire Dragon
    # Since I added them in that order, popping(0) will retrieve them.

    for _ in range(3):
        # card = deck.shuffle()  # Shuffle before drawing
        card = deck.draw_card()
        if card:
            type_str = get_type_str(card)
            print(f"Drew: {card.name} ({type_str})")
            play_result = card.play({})
            print(f"Play result: {play_result}")
            print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
