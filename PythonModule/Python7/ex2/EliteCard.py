from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 defense: int, health: int, magic_power: int,
                 mana_pool: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.health = health
        self.magic_power = magic_power
        self.mana_pool = mana_pool

    def play(self, game_state: dict) -> dict:
        return {"action": "Playing EliteCard", "name": self.name}

    def attack(self, target: str) -> dict:
        return {"attacker": self.name, "target": 'Enemy',
                "damage": self.attack_power, "combat_type": "Melee"}

    def defend(self, incoming_damage: int) -> dict:
        damage_after_defense = max(0, incoming_damage - self.defense)
        self.health -= damage_after_defense
        return {"action": "Defending", "incoming_damage": incoming_damage,
                "damage_after_defense": damage_after_defense,
                "remaining_health": self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {"action": "Casting spell", "spell_name": spell_name,
                "targets": targets, "magic_power_used": self.magic_power}

    def channel_mana(self, amount: int) -> dict:
        return {"action": "Channeling mana", "amount": amount}

    def get_magic_stats(self) -> dict:
        return {"magic_power": self.magic_power, "mana_pool": self.mana_pool}

    def get_combat_stats(self) -> dict:
        return {"attack_power": self.attack_power, "defense": self.defense,
                "health": self.health}
