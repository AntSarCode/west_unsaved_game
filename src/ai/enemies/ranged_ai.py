from base_ai import EnemyAI


class RangedEnemyAI(EnemyAI):
    def __init__(self, name, patrol_points=None):
        super().__init__(name, patrol_points)

    def idle_behavior(self, blackboard):
        # Idle or patrol with alertness
        print(f"{self.name} is on lookout duty.")

    def alerted_behavior(self, blackboard):
        # Look for elevated or covered position
        print(f"{self.name} is finding high ground...")
        if blackboard.get('player_visible', False):
            self.state = 'Engaged'

    def combat_behavior(self, blackboard):
        # Attempt to shoot at player from distance
        target = blackboard.get('player_position')
        if target:
            print(f"{self.name} takes aim and fires at the player!")
        else:
            print(f"{self.name} is scanning for targets...")
            self.state = 'Alerted'
