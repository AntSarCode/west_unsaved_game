from ursina import time, Audio

weapon_types = {
    "rifle": {
        "name": "Rifle",
        "category": "Primary",
        "description": "Versatile and mid-range. Balanced between power and rate of fire.",
        "range": 60,
        "damage": 35,
        "fire_rate": 0.5,
        "reload_time": 2.5,
        "ammo_capacity": 8,
        "reserve_ammo": 56,
        "sound_fire": "assets/sounds/rifle_fire.wav",
        "sound_reload": "assets/sounds/rifle_reload.wav",
        "animation_reload": "reload_rifle",
    },
    "shotgun": {
        "name": "Shotgun",
        "category": "Primary",
        "description": "Close-range powerhouse with spread damage.",
        "range": 20,
        "damage": 70,
        "fire_rate": 1.0,
        "reload_time": 3.0,
        "ammo_capacity": 4,
        "reserve_ammo": 28,
        "sound_fire": "assets/sounds/shotgun_fire.wav",
        "sound_reload": "assets/sounds/shotgun_reload.wav",
        "animation_reload": "reload_shotgun",
    },
    "sniper": {
        "name": "Sniper",
        "category": "Primary",
        "description": "High damage, long-range, low fire rate.",
        "range": 90,
        "damage": 100,
        "fire_rate": 1.5,
        "reload_time": 3.5,
        "ammo_capacity": 1,
        "reserve_ammo": 18,
        "sound_fire": "assets/sounds/sniper_fire.wav",
        "sound_reload": "assets/sounds/sniper_reload.wav",
        "animation_reload": "reload_sniper",
    },
    "pistol": {
        "name": "Pistol",
        "category": "Secondary",
        "description": "Low damage but fast draw and reload. Effective backup.",
        "range": 30,
        "damage": 25,
        "fire_rate": 0.35,
        "reload_time": 1.5,
        "ammo_capacity": 6,
        "reserve_ammo": 30,
        "sound_fire": "assets/sounds/pistol_fire.wav",
        "sound_reload": "assets/sounds/pistol_reload.wav",
        "animation_reload": "reload_pistol",
    },
    "smg": {
        "name": "SMG",
        "category": "Primary",
        "description": "Fast-firing short-range weapon with high mobility.",
        "range": 35,
        "damage": 20,
        "fire_rate": 0.1,
        "reload_time": 2.0,
        "ammo_capacity": 30,
        "reserve_ammo": 120,
        "sound_fire": "assets/sounds/smg_fire.wav",
        "sound_reload": "assets/sounds/smg_reload.wav",
        "animation_reload": "reload_smg",
    },
    "melee": {
        "name": "Melee",
        "category": "Special",
        "description": "Silent and fast. Useful for stealth takedowns.",
        "range": 3,
        "damage": 50,
        "fire_rate": 1.0,
        "reload_time": 0,
        "ammo_capacity": None,
        "reserve_ammo": None,
    }
}

class Weapon:
    def __init__(self, weapon_data):
        self.name = weapon_data["name"]
        self.category = weapon_data["category"]
        self.description = weapon_data["description"]
        self.range = weapon_data["range"]
        self.damage = weapon_data["damage"]
        self.fire_rate = weapon_data["fire_rate"]
        self.reload_time = weapon_data["reload_time"]
        self.ammo_capacity = weapon_data["ammo_capacity"]
        self.reserve_ammo = weapon_data.get("reserve_ammo")

        self.sound_fire = weapon_data.get("sound_fire")
        self.sound_reload = weapon_data.get("sound_reload")
        self.animation_reload = weapon_data.get("animation_reload")

        self.ammo = self.ammo_capacity if self.ammo_capacity is not None else None
        self.last_shot_time = 0
        self.is_reloading = False
        self.reload_start_time = 0

    def fire(self):
        if self.is_reloading:
            print(f"{self.name} is reloading.")
            return False

        if self.ammo_capacity is not None and self.ammo <= 0:
            print(f"{self.name} is out of ammo.")
            return False

        now = time.time()
        if now - self.last_shot_time < self.fire_rate:
            print(f"{self.name} cooling down.")
            return False

        self.last_shot_time = now
        if self.ammo_capacity is not None:
            self.ammo -= 1

        if self.sound_fire:
            Audio(self.sound_fire)

        print(f"Fired {self.name}. Ammo left: {self.ammo if self.ammo is not None else '∞'}")
        return True

    def start_reload(self):
        if self.ammo_capacity is None:
            print(f"{self.name} does not need to reload.")
            return

        if self.reserve_ammo == 0:
            print(f"{self.name} has no reserve ammo.")
            return

        self.is_reloading = True
        self.reload_start_time = time.time()

        if self.sound_reload:
            Audio(self.sound_reload)

        if self.animation_reload:
            print(f"Playing reload animation: {self.animation_reload}")

        print(f"Reloading {self.name}...")

    def update_reload(self):
        if not self.is_reloading:
            return

        if time.time() - self.reload_start_time >= self.reload_time:
            needed = self.ammo_capacity - self.ammo
            to_reload = min(needed, self.reserve_ammo)
            self.ammo += to_reload
            self.reserve_ammo -= to_reload
            self.is_reloading = False
            print(f"{self.name} reloaded. Ammo: {self.ammo}/{self.ammo_capacity}, Reserve: {self.reserve_ammo}")


def validate_weapons():
    for key, weapon in weapon_types.items():
        required = ["name", "category", "description", "range", "damage", "fire_rate", "reload_time"]
        for field in required:
            if field not in weapon:
                print(f"Weapon '{key}' missing required field: {field}")
