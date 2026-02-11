from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        rating: int = 1000,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.card_id = card_id
        self.attack_power = attack_power
        self.defense_power = defense
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        return {
            "action": "play",
            "card": self.name,
            "info": "Card played in tournament"
        }

    def attack(self, target) -> dict:
        t_name = target.name if hasattr(target, 'name') else str(target)
        return {
            "action": "attack",
            "attacker": self.name,
            "target": t_name,
            "damage": self.attack_power
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense_power)
        return {
            "action": "defend",
            "defender": self.name,
            "damage_mitigated": self.defense_power,
            "damage_taken": damage_taken
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense_power,
            "health": 100
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        stats = self.get_card_info()
        stats.update(self.get_combat_stats())
        stats.update(self.get_rank_info())
        stats["id"] = self.card_id
        return stats
