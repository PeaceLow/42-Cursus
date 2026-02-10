from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        try:
            if attack < 0 or health < 0:
                raise ValueError("Attack and health must be non-negative.")
            self.attack = attack
            self.health = health
        except Exception as e:
            print(f"Error initializing CreatureCard: {e}")

    def play(self, game_state: dict) -> dict:
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Creature summoned to battlefield"}

    def get_card_info(self) -> dict:
        return super().get_card_info() | {"type": "Creature",
                                          "attack": self.attack,
                                          "health": self.health}

    def attack_target(self, target: str) -> dict:
        return {"attacker": self.name, "target": target,
                "damage_dealt": self.attack, "combat_resolved": True}
