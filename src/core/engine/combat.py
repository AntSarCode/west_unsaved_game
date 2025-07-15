from src.users.status_effects import status_effect_types
from src.weapons.weapon_stats import weapon_characteristics

def calculate_damage(attacker, target, weapon_key):
    weapon = weapon_characteristics.get(weapon_key)
    if not weapon:
        print(f"Unknown weapon: {weapon_key}")
        return 0

    base_damage = weapon["damage"]

    # Check for bonus or penalty multipliers
    damage = base_damage
    if hasattr(attacker, "damage_multiplier"):
        damage *= attacker.damage_multiplier
    if hasattr(target, "damage_resistance"):
        damage *= (1 - target.damage_resistance)

    return int(damage)

def apply_damage(attacker, target, damage):
    if hasattr(target, "take_damage"):
        target.take_damage(damage, source=attacker)
    else:
        print(f"{target} has no take_damage() method.")

def handle_death(player):
    print(f"{player.name} has died.")
    # Player death is now handled in player.take_damage()
    # Consider calling game state updates, drops, or kill feed here if needed

def apply_on_hit_effects(target, weapon_key):
    weapon = weapon_characteristics.get(weapon_key)
    if not weapon:
        return

    if "on_hit_effect" in weapon:
        effect = weapon["on_hit_effect"]
        if effect in status_effect_types:
            target.apply_status_effect(effect)
