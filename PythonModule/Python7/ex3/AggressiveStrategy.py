from .GameStrategy import GameStrategy
import re

class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        hand.sort(key=lambda c: c.cost)
        
        mana_pool = 5
        current_mana = 0
        cards_played = []
        damage_dealt = 0
        
        for card in hand:
            if current_mana + card.cost <= mana_pool:
                current_mana += card.cost
                cards_played.append(card.name)
                
                if hasattr(card, 'attack'):
                    damage_dealt += card.attack
                elif hasattr(card, 'effect_type'):
                     desc = str(card.effect_type).lower()
                     if "damage" in desc:
                         nums = re.findall(r'\d+', desc)
                         if nums:
                             damage_dealt += int(nums[0])
                         else:
                             damage_dealt += 3
            
        return {
            'cards_played': cards_played,
            'mana_used': current_mana,
            'targets_attacked': self.prioritize_targets(["Enemy Player"]),
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return [t for t in available_targets if "Enemy" in t or "Player" in t]
