from boss_base import BossAI
from ai.behavior_trees.generic_tree import Selector, Sequence, Action, Condition


class ElderElk(BossAI):
    def __init__(self):
        super().__init__(name="Elder Elk", max_health=1000)
        self.behavior_phase_1 = self._build_phase_1_tree()
        self.behavior_phase_2 = self._build_phase_2_tree()

    def evaluate_behavior(self, blackboard):
        if self.phase == 1:
            self.behavior_phase_1.run(blackboard)
        else:
            self.behavior_phase_2.run(blackboard)

    def trigger_phase_transition(self):
        print("Elder Elk roars and enters Phase 2!")
        self.phase = 2

    def _build_phase_1_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('player_nearby', False)),
                Action(lambda bb: print("Elder Elk charges with antlers!"))
            ]),
            Action(lambda bb: print("Elder Elk surveys the clearing..."))
        ])

    def _build_phase_2_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('player_nearby', False)),
                Action(lambda bb: print("Elder Elk summons spectral vines!"))
            ]),
            Action(lambda bb: print("Elder Elk stomps, shaking the ground!"))
        ])
