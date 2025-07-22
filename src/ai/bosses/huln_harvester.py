from ai.bosses.boss_base import BossAI
from ai.behavior_trees.generic_tree import Selector, Sequence, Action, Condition


class HulnHarvester(BossAI):
    def __init__(self):
        super().__init__(name="Huln the Harvester", max_health=2000)
        self.behavior_phase_1 = self._build_phase_1_tree()
        self.behavior_phase_2 = self._build_phase_2_tree()

    def evaluate_behavior(self, blackboard):
        if self.phase == 1:
            self.behavior_phase_1.run(blackboard)
        else:
            self.behavior_phase_2.run(blackboard)

    def trigger_phase_transition(self):
        print("Huln bellows: 'You will reap only agony!' and ascends to Phase 2!")
        self.phase = 2

    def _build_phase_1_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('player_nearby', False)),
                Action(lambda bb: print("Huln slams the earth with his sickle-hand!"))
            ]),
            Action(lambda bb: print("Huln watches from his obsidian throne."))
        ])

    def _build_phase_2_tree(self):
        return Selector([
            Sequence([
                Condition(lambda bb: bb.get('any_ally_dead', False)),
                Action(lambda bb: print("Huln channels the spirits of fallen giants!"))
            ]),
            Action(lambda bb: print("Huln grows in size, his skin gleaming with divine glyphs."))
        ])
