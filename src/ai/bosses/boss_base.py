from abc import ABC, abstractmethod


class BossAI(ABC):
    def __init__(self, name, max_health):
        self.name = name
        self.max_health = max_health
        self.current_health = max_health
        self.phase = 1
        self.target = None

    @abstractmethod
    def evaluate_behavior(self, blackboard):
        """
        Evaluate and execute the boss's current behavior.
        Should return an action or state decision.
        """
        pass

    @abstractmethod
    def trigger_phase_transition(self):
        """
        Handle logic for switching phases (e.g., upon reaching a health threshold).
        """
        pass

    def get_target(self):
        """
        Returns the current target for the boss to act upon.
        """
        return self.target

    def set_target(self, target):
        """
        Assign a target to the boss.
        """
        self.target = target

    def take_damage(self, amount):
        """
        Apply damage and check if a phase transition is needed.
        """
        self.current_health -= amount
        if self.should_transition():
            self.trigger_phase_transition()

    def should_transition(self):
        """
        Determine whether the boss should change behavior phases based on health.
        """
        return self.current_health <= self.max_health * 0.5 and self.phase == 1
