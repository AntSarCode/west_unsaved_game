from boss_base import BossAI
from ai.behavior_trees.generic_tree import Selector, Sequence, Action, Condition


class SpiritBreaker(BossAI):
    def __init__(self):
        super().__init__(name="Spirit Breaker", max_health=1400)
        self.behavior_phase_1 = self._build_phase_1_tree()
        self.behavior_phase_2 = self._build_phase_2_tree()

    def evaluate_behavior(self, blackboard):
        if self.phase == 1:
            self.behavior_phase_1.run(blackboard)
        else:
            self.behavior_phase_2.run(blackboard)

    def trigger_phase_transition(self):
        print("Spirit Breaker fractures the veil and enters Phase 2!")
        self.phase = 2

    def _build_phase_1_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('player_casting_spell', False)),
                Action(lambda bb: print("Spirit Breaker silences the caster!"))
            ]),
            Action(lambda bb: print("Spirit Breaker drifts ominously through the battlefield..."))
        ])

    def _build_phase_2_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('multiple_enemies_nearby', False)),
                Action(lambda bb: print("Spirit Breaker unleashes a soul rupture AoE!"))
            ]),
            Action(lambda bb: print("Spirit Breaker phases between planes, reducing damage taken."))
        ])
