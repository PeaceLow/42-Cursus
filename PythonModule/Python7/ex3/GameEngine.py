from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self.factory = None
        self.strategy = None
        self.hand = []
        self.battlefield = []

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self.factory = factory
        self.strategy = strategy
        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        print(f"Available types: {factory.get_supported_types()}")

    def simulate_turn(self) -> dict:
        print("\nSimulating aggressive turn...")
        self.hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell()
        ]

        hand_display = []
        for c in self.hand:
            cost = c.cost
            hand_display.append(f"{c.name} ({cost})")

        print(f"Hand: [{', '.join(hand_display)}]")

        print("\nTurn execution:")
        print(f"Strategy: {self.strategy.get_strategy_name()}")

        result = self.strategy.execute_turn(self.hand, self.battlefield)
        print(f"Actions: {result}")

        return {
            'turns_simulated': 1,
            'strategy_used': self.strategy.get_strategy_name(),
            'total_damage': result.get('damage_dealt', 0),
            'cards_created': len(self.hand)
        }

    def get_engine_status(self) -> dict:
        return {}
