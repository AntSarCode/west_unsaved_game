from src.core.engine.tick import GameClock
from src.core.engine.phases import PhaseState
from utils.combat_utils import apply_damage, apply_on_hit_effects, calculate_damage
from src.core.engine.game_state import GameState


class GameEngine:
    def __init__(self):
        self.clock = GameClock()
        self.phase = PhaseState()
        self.state = GameState()
        self.state.phase_state = self.phase
        self.tick_interval = 1

        # Hook phase ticking into clock
        self.clock.subscribe(self.phase_tick, self.tick_interval)

    def phase_tick(self):
        self.phase.tick()

    def run(self):
        print("Game engine starting...")
        self.clock.run_forever()

    def process_attack(self, attacker, target, weapon_key):
        damage = apply_damage(target, calculate_damage(attacker, target, weapon_key))
        apply_on_hit_effects(target, weapon_key)
        return damage
