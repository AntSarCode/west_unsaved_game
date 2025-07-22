from ai.behavior_trees.generic_tree import Selector, Sequence, Action, Condition

def vendor_behavior_tree():
    return Selector([
        Sequence([
            Condition(lambda bb: bb.get('player_nearby', False)),
            Action(lambda bb: print("Vendor: Welcome! Care to trade?"))
        ]),
        Action(lambda bb: print("Vendor waits silently."))
    ])


def guard_patrol_tree():
    return Selector([
        Sequence([
            Condition(lambda bb: bb.get('player_suspicious', False)),
            Action(lambda bb: print("Guard: Halt! Show your papers."))
        ]),
        Action(lambda bb: print("Guard patrols perimeter."))
    ])


def wanderer_idle_tree():
    return Selector([
        Action(lambda bb: print("Wanderer hums a forgotten tune..."))
    ])


# Registry for dynamic linking (optional convenience)
BEHAVIOR_TREE_REGISTRY = {
    "vendor_behavior_tree": vendor_behavior_tree,
    "guard_patrol_tree": guard_patrol_tree,
    "wanderer_idle_tree": wanderer_idle_tree,
    # Add additional behavior tree functions here as needed
}