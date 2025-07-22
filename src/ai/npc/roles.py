from enum import Enum, auto


class NPCRole(Enum):
    VENDOR = auto()
    QUEST_GIVER = auto()
    GUARD = auto()
    WANDERER = auto()
    STORYTELLER = auto()
    TRAINER = auto()
    HEALER = auto()
    CITIZEN = auto()


class RoleBehaviorMapper:
    """
    Utility class to associate roles with expected behavior types or tree roots.
    """
    @staticmethod
    def get_behavior_tree(role):
        if role == NPCRole.VENDOR:
            return "vendor_behavior_tree"
        elif role == NPCRole.QUEST_GIVER:
            return "quest_giver_behavior_tree"
        elif role == NPCRole.GUARD:
            return "guard_patrol_tree"
        elif role == NPCRole.WANDERER:
            return "wanderer_idle_tree"
        elif role == NPCRole.STORYTELLER:
            return "story_idle_tree"
        elif role == NPCRole.TRAINER:
            return "trainer_interaction_tree"
        elif role == NPCRole.HEALER:
            return "healing_support_tree"
        elif role == NPCRole.CITIZEN:
            return "default_citizen_behavior"
        else:
            return "generic_idle_tree"
