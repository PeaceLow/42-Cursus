from abc import ABC, abstractmethod


class Magical(ABC):
    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        return {"action": "Channeling mana", "amount": amount}

    @abstractmethod
    def get_magic_stats(self) -> dict:
        return {"magic_power": 0, "mana_pool": 0}
