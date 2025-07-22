from boss_base import BossAI
from ai.behavior_trees.generic_tree import Selector, Sequence, Action, Condition


class DrownedSigil(BossAI):
    def __init__(self):
        super().__init__(name="Drowned Sigil", max_health=1200)
        self.behavior_phase_1 = self._build_phase_1_tree()
        self.behavior_phase_2 = self._build_phase_2_tree()

    def evaluate_behavior(self, blackboard):
        if self.phase == 1:
            self.behavior_phase_1.run(blackboard)
        else:
            self.behavior_phase_2.run(blackboard)

    def trigger_phase_transition(self):
        print("Drowned Sigil mutates and enters Phase 2!")
        self.phase = 2

    def _build_phase_1_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('player_nearby', False)),
                Action(lambda bb: print("Drowned Sigil casts water bolt!"))
            ]),
            Action(lambda bb: print("Drowned Sigil levitates and emits static..."))
        ])

    def _build_phase_2_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('player_low_health', False)),
                Action(lambda bb: print("Drowned Sigil siphons vitality from the weak!"))
            ]),
            Action(lambda bb: print("Drowned Sigil floods the arena with spectral tides!"))
        ])
