status_effect_types = {
    "allure": {
        "name": "Allure",
        "description": "Disables weapon and ability use and causes enemies to walk toward the effect applicator.",
        "effect_type": "Crowd Control",
        "attract": True,
        "duration": 3,
    },
    "bleed": {
        "name": "Bleed",
        "description": "Slows movement slightly and applies light DoT.",
        "effect_type": "DoT",
        "damage_over_time": True,
        "movement_penalty": 0.1,
        "duration": 9,
        "tick_interval": 1.5,
    },
    "burn": {
        "name": "Burn",
        "description": "Deals fire damage over time.",
        "effect_type": "DoT",
        "damage_over_time": True,
        "duration": 4,
        "tick_interval": 1,
    },
    "fear": {
        "name": "Fear",
        "description": "Causes the target to flee in a random direction for 2 seconds. Target cannot attack or use abilities while fleeing.",
        "effect_type": "Crowd Control",
        "flee": True,
        "duration": 2.5,
    },
    "freeze": {
        "name": "Freeze",
        "description": "Temporarily immobilizes the target and applies light DoT.",
        "effect_type": "Crowd Control",
        "immobilize": True,
        "damage_over_time": True,
        "duration": 2,
        "tick_interval": 1,
    },
    "mark": {
        "name": "Marked",
        "description": "Target takes increased damage from all sources.",
        "effect_type": "Debuff",
        "damage_multiplier": 1.25,
        "duration": 6,
    },
    "poison": {
        "name": "Poison",
        "description": "Deals poison damage over time and reduces healing effectiveness.",
        "effect_type": "DoT",
        "damage_over_time": True,
        "healing_penalty": 0.5,
        "duration": 4,
        "tick_interval": 1,
    },
    "slow": {
        "name": "Slow",
        "description": "Reduces movement speed significantly.",
        "effect_type": "Debuff",
        "movement_penalty": 0.4,
        "duration": 4,
    },
    "stealth": {
        "name": "Stealth",
        "description": "Player gains 20% speed boost and makes 80% less noise for 12 seconds, and is invisible to enemies for 5 seconds. Player cannot deal damage while invisible, and can be detected by certain abilities.",
        "effect_type": "Buff",
        "invisibility": True,
        "speed_boost": 0.2,
        "damage_penalty": 1.0,
        "duration": 5,
        "tick_interval": 1,
    },
    "stun": {
        "name": "Stun",
        "description": "Temporarily slows movement and disables ADS.",
        "effect_type": "Crowd Control",
        "movement_penalty": 0.75,
        "duration": 2,
    },
}

def validate_status_effects():
    """Validate presence of core fields and ensure known structure."""
    required_keys = {
        "name", "description", "duration"
    }
    issues = []
    for key, props in status_effect_types.items():
        missing = required_keys - props.keys()
        if missing:
            issues.append((key, f"Missing keys: {missing}"))
        if 'effect_type' not in props:
            issues.append((key, "Missing 'effect_type' field"))
    return issues
