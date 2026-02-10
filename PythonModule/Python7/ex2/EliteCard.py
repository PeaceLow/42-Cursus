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
        damage_taken = 0
        damage_taken = max(0, incoming_damage - self.defense)
        self.health -= damage_taken
        return {"defender": self.name, "damage_taken": damage_taken,
                "damage_blocked": self.defense,
                "still_alive": self.health > 0}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self.mana_pool < self.magic_power:
            return {"error": "Not enough mana to cast the spell"}
        self.mana_pool -= self.magic_power
        return {"caster": self.name, "spell": spell_name,
                "targets": targets,
                "mana_used": self.magic_power}

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {"channeled": amount, "total_mana": self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {"magic_power": self.magic_power, "mana_pool": self.mana_pool}

    def get_combat_stats(self) -> dict:
        return {"attack_power": self.attack_power, "defense": self.defense,
                "health": self.health}
