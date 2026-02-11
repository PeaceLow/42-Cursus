from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int |
                        None = None) -> CreatureCard:
        if (name_or_power == "dragon" or
                (isinstance(name_or_power, int) and
                 name_or_power and name_or_power > 4)):
            return CreatureCard("Fire Dragon", 5, "Rare", 5, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    def create_spell(self, name_or_power: str | int |
                     None = None) -> SpellCard:
        if name_or_power == "fireball":
            return SpellCard("Fireball", 4, "Rare", "Deals 5 damage")
        return SpellCard("Lightning Bolt", 3, "Common", "Deals 6 damage")

    def create_artifact(self, name_or_power: str | int |
                        None = None) -> ArtifactCard:
        return ArtifactCard("Mana Ring", 1, "Rare", 3, "Adds 1 mana")

    def create_themed_deck(self, size: int) -> dict:
        deck = {'creatures': [], 'spells': [], 'artifacts': []}
        return deck

    def get_supported_types(self) -> dict:
        return {'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'], 'artifacts': ['mana_ring']}
