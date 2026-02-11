from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main():
    print("=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    # "Fire Dragon (ID: dragon_001)" "Rating: 1200"
    c1 = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary",
                        20, 15, 1200)

    # "Ice Wizard (ID: wizard_001)" "Rating: 1150"
    c2 = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 18, 12,
                        1150)

    platform.register_card(c1)
    platform.register_card(c2)

    # Output formatting
    print(f"{c1.name} (ID: {c1.card_id}):")
    # Hardcoded interface list as per example output
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {c1.rating}")
    print(f"- Record: {c1.wins}-{c1.losses}\n")

    print(f"{c2.name} (ID: {c2.card_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {c2.rating}")
    print(f"- Record: {c2.wins}-{c2.losses}\n")

    print("Creating tournament match...")
    result = platform.create_match(c1.card_id, c2.card_id)
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        record = f"{card.wins}-{card.losses}"
        print(f"{i}. {card.name} - Rating: {card.rating} ({record})")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
