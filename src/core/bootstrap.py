from ursina import load_texture
from pathlib import Path
from src.config.teams.alliance import AllianceManager
from src.config.metrics.constants import ALLIANCE_MAX
from src.config.metrics.map import load_map_config
from src.utils.match_logger import match_logger

ASSET_PATHS = {
    "models": Path("assets/models"),
    "textures": Path("assets/textures"),
    "audio": Path("assets/audio"),
    "maps": Path("data/map_drafts")
}

def verify_assets():
    for name, path in ASSET_PATHS.items():
        if not path.exists():
            print(f"[BOOTSTRAP WARNING] Missing {name} folder at: {path}")
        else:
            print(f"[BOOTSTRAP] {name.capitalize()} OK")

def bootstrap_game_environment():
    print(f"[BOOTSTRAP] Initializing game environment...")

    verify_assets()
    match_logger()

    map_config = load_map_config()
    alliances = AllianceManager(ALLIANCE_MAX)

    print(f"[BOOTSTRAP] Loaded map config with {len(map_config['zones'])} zones")
    print(f"[BOOTSTRAP] Alliances initialized: {alliances}")

    return {
        "map_config": map_config,
        "alliances": alliances,
    }
