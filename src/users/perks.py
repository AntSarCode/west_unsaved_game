PERKS = {
    'Deadeye': {
        'weapon_range_bonus': 0.2,
        'weapon_ammo_bonus': 0.15,
        'speed_penalty': 1,
        'economy_cost': 400,
    },
    'Rager': {
        'health_bonus': 50,
        'speed_penalty': 2,
        'economy_cost': 300,
    },
    'Engineer': {
        'economy_bonus': 0.25,
        'can_repair': True,
        'can_sabotage': True,
        'combat_penalty': 0.1,
        'economy_cost': 500,
    },
    'Graverobber': {
        'stealth': True,
        'loot_bonus': 0.15,
        'can_steal': True,
        'speed_bonus': 2,
        'health_penalty': 20,
        'economy_cost': 450,
    },
    'Doctor': {
        'can_heal_others': True,
        'heal_others_amount': 30,
        'can_heal_self': True,
        'heal_self_amount': 50,
        'weapon_restriction': 'no_heavy',
        'economy_cost': 550,
    },
    "Gambler": {
        "crit_chance_bonus": 0.1,
        "crit_fail_chance": 0.05,
        "economy_bonus": 0.1,
        "random_buff_on_spawn": True,
        "economy_cost": 500
    },
    "Witch": {
        "ability_cooldown_reduction": 0.15,
        "fog_resistance": True,
        "aura_visibility": True,
        "health_penalty": 30,
        "economy_cost": 450
    },
    "Wastelander": {
        "heat_resistance": True,
        "loot_bonus": 0.2,
        "melee_bonus": 0.1,
        "speed_bonus_in_collapse": 2,
        "economy_cost": 400
    },
    "Lawman": {
        "team_buff_radius": 10,
        "team_morale_boost": True,
        "duel_damage_bonus": 0.2,
        "reload_penalty": 0.15,
        "economy_cost": 550
    },
    "Preacher": {
        "ally_revive_speed": 2.0,
        "fear_aura": 5,
        "ammo_capacity_penalty": 0.2,
        "economy_cost": 500
    },
    "Moonshiner": {
        "stamina_regen_bonus": 0.25,
        "can_buff_allies": True,
        "accuracy_penalty": 0.1,
        "fire_damage_weakness": True,
        "economy_cost": 450
    },
    "Widowmaker": {
        "sniper_crit_bonus": 0.25,
        "no_melee": True,
        "speed_penalty": 1,
        "economy_cost": 475
    },
    "Dustcaller": {
        "camouflage_bonus": True,
        "bonus_damage_while_stationary": 0.15,
        "vision_penalty_moving": True,
        "economy_cost": 425
    },
    "Tinkerer": {
        "trap_placement_bonus": True,
        "device_hack_speed": 1.5,
        "reduced_weapon_reload": 0.2,
        "health_penalty": 15,
        "economy_cost": 475
    },
    "Scorpion": {
        "poison_resistance": True,
        "melee_bleed_effect": True,
        "health_regen_delay": 3,
        "economy_cost": 425
    },
    "Native": {
        "tracking_bonus": True,
        "terrain_speed_bonus": 0.15,
        "reduced_footstep_noise": True,
        "economy_cost": 475
    },
    "Charlatan": {
        "disguise_ability": True,
        "voice_mimicry": True,
        "low_trust_penalty": 0.2,
        "economy_cost": 500
    },
    "Holy Spirit": {
        "revive_aura_radius": 5,
        "fear_immunity": True,
        "cannot_use_ranged": True,
        "economy_cost": 450
    },
    "Deputy": {
        "team_respawn_discount": 0.2,
        "objective_bonus": 0.1,
        "reduced_loot_gain": 0.1,
        "economy_cost": 475
    },
    "Maiden": {
        "allure_effect_radius": 3,
        "temporary_alliance_on_contact": True,
        "health_penalty": 0.15,
        "economy_cost": 425
    },
    "Undead": {
        "revive_on_death_once": True,
        "immune_to_bleed": True,
        "immune_to_allure": True,
        "health_cap": 75,
        "fire_damage_vulnerability": 0.25,
        "ice_damage_vulnerability": 0.25,
        "economy_cost": 500
    }
}

# --- Perk Type Categorization ---
PERK_CATEGORIES = {
    'combat': ['Deadeye', 'Rager', 'Widowmaker', 'Scorpion', 'Witch', 'Lawman'],
    'support': ['Doctor', 'Moonshiner', 'Preacher', 'Holy Spirit', 'Deputy'],
    'stealth': ['Graverobber', 'Dustcaller', 'Native', 'Charlatan', 'Maiden'],
    'economy': ['Engineer', 'Gambler', 'Deputy'],
    'sabotage': ['Engineer', 'Tinkerer', 'Charlatan'],
    'mobility': ['Wastelander', 'Native', 'Undead'],
    'resurrection': ['Undead', 'Holy Spirit'],
}

# --- Perk Validation Function ---
def validate_perks():
    invalid_perks = []
    for name, data in PERKS.items():
        if 'economy_cost' not in data:
            invalid_perks.append((name, 'Missing economy_cost'))
        if not isinstance(data, dict):
            invalid_perks.append((name, 'Perk definition is not a dictionary'))
    return invalid_perks
