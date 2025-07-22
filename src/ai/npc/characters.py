from roles import NPCRole, RoleBehaviorMapper


class NPC:
    def __init__(self, name, role, position):
        self.name = name
        self.role = role  # Should be instance of NPCRole
        self.position = position
        self.behavior_tree = RoleBehaviorMapper.get_behavior_tree(role)

    def interact(self):
        print(f"{self.name} the {self.role.name.title()} greets you.")

    def update(self, _):
        """
        Placeholder for future behavior tree integration.
        """
        print(f"{self.name} runs behavior: {self.behavior_tree}")


# Example NPC roster
if __name__ == "__main__":
    vendor = NPC("Lars", NPCRole.VENDOR, (10, 0, 5))
    guard = NPC("Rhea", NPCRole.GUARD, (15, 0, -3))

    blackboard = {}  # Placeholder context

    vendor.interact()
    vendor.update(blackboard)

    guard.interact()
    guard.update(blackboard)
