import os
import json
from weapons import Weapon

WEAPON_DATA_DIR = "weapons/data"

weapon_library = {}


def load_weapon_data(folder):
    """
    Loads all .json files from the specified folder into the weapon library.
    """
    for filename in os.listdir(folder):
        if filename.endswith(".json"):
            filepath = os.path.join(folder, filename)
            with open(filepath, "r") as f:
                try:
                    data = json.load(f)
                    key = data["name"].lower().replace(" ", "_").replace("'", "")
                    weapon_library[key] = Weapon(data)
                except Exception as e:
                    print(f"Failed to load {filename}: {e}")


def build_weapon_library():
    print("\n[WeaponLoader] Loading all weapons from weapons/data...")
    load_weapon_data(WEAPON_DATA_DIR)
    print(f"[WeaponLoader] Loaded {len(weapon_library)} weapons into library.")


build_weapon_library()
