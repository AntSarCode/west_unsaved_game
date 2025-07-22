from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def run(self, bb):
        """
        Execute this node's logic.
        Return True if successful, False otherwise.
        """
        pass


class Selector(Node):
    def __init__(self, children):
        self.children = children

    def run(self, bb):
        for child in self.children:
            if child.run(bb):
                return True
        return False


class Sequence(Node):
    def __init__(self, children):
        self.children = children

    def run(self, bb):
        for child in self.children:
            if not child.run(bb):
                return False
        return True


class Action(Node):
    def __init__(self, func):
        self.func = func

    def run(self, bb):
        # Executes a callable and expects True/False return for success/failure
        return self.func(bb)


class Condition(Node):
    def __init__(self, condition_func):
        self.condition_func = condition_func

    def run(self, bb):
        # Evaluates condition; if True, proceeds, else fails
        return self.condition_func(bb)


# Example usage
if __name__ == "__main__":
    def is_enemy_visible(bb):
        return bb.get('enemy_visible', False)

    def attack(_):
        print("Attacking enemy!")
        return True

    tree = Selector([
        Sequence([
            Condition(is_enemy_visible),
            Action(attack)
        ])
    ])

    # Sample blackboard (shared AI context)
    blackboard = {'enemy_visible': True}
    tree.run(blackboard)
