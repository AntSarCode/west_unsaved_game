from ai.enemies.base_ai import EnemyAI


class MeleeEnemyAI(EnemyAI):
    def __init__(self, name, patrol_points=None):
        super().__init__(name, patrol_points)

    def idle_behavior(self, blackboard):
        # Simple patrol logic or stand in place
        print(f"{self.name} is idling.")

    def alerted_behavior(self, blackboard):
        # Investigate source of sound or movement
        print(f"{self.name} is investigating the disturbance...")
        if blackboard.get('player_visible', False):
            self.state = 'Engaged'

    def combat_behavior(self, blackboard):
        # Close the distance and attempt melee attack
        target = blackboard.get('player_position')
        if target:
            print(f"{self.name} charges at the player and attacks!")
        else:
            print(f"{self.name} is ready to fight but can't find the target.")
            self.state = 'Alerted'
