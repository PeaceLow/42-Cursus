from .TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self):
        self.cards = {}  # id -> card
        self.matches = []

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.cards.get(card1_id)
        c2 = self.cards.get(card2_id)
        if not c1 or not c2:
            return {"error": "Card not found"}

        # Simple match logic:
        # Score = Attack + Random(0-5)
        # Winner gets +16 rating, loser -16.

        score1 = c1.attack_power + random.randint(0, 5)
        score2 = c2.attack_power + random.randint(0, 5)

        # Handle ties randomly
        if score1 == score2:
            if random.choice([True, False]):
                score1 += 1
            else:
                score2 += 1

        if score1 > score2:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)

        rating_change = 16
        winner.rating += rating_change
        loser.rating -= rating_change

        self.matches.append({
            "winner": winner.card_id,
            "loser": loser.card_id
        })

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating
        }

    def get_leaderboard(self) -> list:
        all_cards = list(self.cards.values())
        # Sort by rating descending
        all_cards.sort(key=lambda c: c.calculate_rating(), reverse=True)
        return all_cards

    def generate_tournament_report(self) -> dict:
        ratings = [c.calculate_rating() for c in self.cards.values()]
        avg = sum(ratings) / len(ratings) if ratings else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self.matches),
            "avg_rating": avg,
            "platform_status": "active"
        }
