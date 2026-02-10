from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card) -> None:
        if isinstance(card, Card):
            self.cards.append(card)
        else:
            print("Error: Only cards can be added to the deck.")

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for card in self.cards:
            class_name = card.__class__.__name__
            if class_name == "CreatureCard":
                creatures += 1
            elif class_name == "SpellCard":
                spells += 1
            elif class_name == "ArtifactCard":
                artifacts += 1

            total_cost += card.cost

        total_cards = len(self.cards)
        avg_cost = total_cost / total_cards if total_cards > 0 else 0.0
        avg_cost = f"{avg_cost:.1f}"  # Format to 2 decimal places

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
