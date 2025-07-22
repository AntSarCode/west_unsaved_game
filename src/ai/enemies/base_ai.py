from abc import ABC, abstractmethod


class EnemyAI(ABC):
    def __init__(self, name, patrol_points=None):
        self.name = name
        self.state = 'Idle'
        self.patrol_points = patrol_points or []
        self.current_target = None

    def update(self, blackboard):
        """
        Main update loop for decision making. Routes behavior based on current state.
        """
        if self.state == 'Idle':
            self.idle_behavior(blackboard)
        elif self.state == 'Alerted':
            self.alerted_behavior(blackboard)
        elif self.state == 'Engaged':
            self.combat_behavior(blackboard)

    @abstractmethod
    def idle_behavior(self, blackboard):
        """
        Define behavior when in Idle state (e.g., patrol, stand).
        """
        pass

    @abstractmethod
    def alerted_behavior(self, blackboard):
        """
        Define behavior when suspicious or investigating.
        """
        pass

    @abstractmethod
    def combat_behavior(self, blackboard):
        """
        Define combat behavior when engaging a target.
        """
        pass

    def detect_enemy(self, blackboard):
        """
        Basic vision or proximity detection logic.
        Transition to 'Alerted' or 'Engaged' as needed.
        """
        if blackboard.get('player_visible', False):
            self.state = 'Engaged'
        elif blackboard.get('suspicious_noise', False):
            self.state = 'Alerted'

    def take_damage(self, amount):
        """
        Optional: Modify health or trigger reactions.
        """
        print(f"{self.name} took {amount} damage!")
