import json
from pathlib import Path

def load_map_config(path="data/map_drafts/map_config.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] Map config file not found at: {path}")
        return {"zones": []}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Failed to parse map config JSON: {e}")
        return {"zones": []}

MAP_WIDTH = 100  # arbitrary units
MAP_HEIGHT = 100

# Node format: {'name': str, 'x': int, 'y': int, 'type': str, 'capture_zone': bool}
MAP_NODES = [
    {'name': 'Outpost North', 'x': 15, 'y': 20, 'type': 'control', 'capture_zone': True},
    {'name': 'Shatterpoint', 'x': 50, 'y': 50, 'type': 'boss', 'capture_zone': False},
    {'name': 'Dustspire South', 'x': 85, 'y': 80, 'type': 'control', 'capture_zone': True},
    {'name': 'Hidden Cache', 'x': 40, 'y': 90, 'type': 'loot', 'capture_zone': False},
    {'name': 'Altar of Horns', 'x': 75, 'y': 25, 'type': 'objective', 'capture_zone': False},
]

# Optional: terrain types
TERRAIN_TYPES = {
    'flat': 1.0,
    'forest': 0.85,
    'water': 0.5,
    'mountain': 0.3,
}
