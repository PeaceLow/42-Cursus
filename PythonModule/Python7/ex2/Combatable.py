from abc import ABC, abstractmethod


class Combatable(ABC):
    @abstractmethod
    def attack(self, target: str) -> dict:
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        return {"attack_power": 0, "defense": 0, "health": 0}
