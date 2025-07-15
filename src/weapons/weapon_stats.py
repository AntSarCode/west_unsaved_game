weapon_characteristics = {
    "rifle": {
        "damage": 35,
        "fire_rate": 0.5,  # Seconds per shot
        "reload_time": 2.5,
        "ammo_capacity": 8,
        "range": "medium",
        "recoil": "moderate",
    },
    "shotgun": {
        "damage": 70,
        "fire_rate": 1.0,
        "reload_time": 3.0,
        "ammo_capacity": 2,
        "range": "short",
        "recoil": "high",
    },
    "sniper": {
        "damage": 100,
        "fire_rate": 1.5,
        "reload_time": 3.5,
        "ammo_capacity": 1,
        "range": "long",
        "recoil": "very high",
    },
    "pistol": {
        "damage": 25,
        "fire_rate": 0.35,
        "reload_time": 1.5,
        "ammo_capacity": 6,
        "range": "short",
        "recoil": "low",
    },
    "smg": {
        "damage": 20,
        "fire_rate": 0.1,
        "reload_time": 2.0,
        "ammo_capacity": 12,
        "range": "short",
        "recoil": "low",
    },
    "melee": {
        "damage": 50,
        "fire_rate": 1.0,
        "reload_time": 0.0,
        "ammo_capacity": None,
        "range": "melee",
        "recoil": "none",
    },
}

def validate_weapon_characteristics():
    for weapon, stats in weapon_characteristics.items():
        required = ["damage", "fire_rate", "reload_time", "ammo_capacity", "range", "recoil"]
        for field in required:
            if field not in stats:
                print(f"{weapon} missing required field: {field}")
