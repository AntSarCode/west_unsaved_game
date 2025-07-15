import os
import json
from datetime import datetime, timezone
from typing import Dict, Any

LOG_DIR = "logs"

class MatchLogger:
    def __init__(self):
        os.makedirs(LOG_DIR, exist_ok=True)
        self.session_data: Dict[str, Any] = {
            "start_time": datetime.now(timezone.utc).isoformat(),
            "events": []
        }
        self.match_id = datetime.now(timezone.utc).strftime("match_%Y%m%d_%H%M%S")

    def log_event(self, event_type: str, data: Dict[str, Any]):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "type": event_type,
            "data": data
        }
        self.session_data["events"].append(event)

    def save_log(self):
        filepath = os.path.join(LOG_DIR, f"{self.match_id}.json")
        with open(filepath, 'w') as f:
            json.dump(self.session_data, f, indent=2)
        print(f"Match log saved to {filepath}")

    def reset(self):
        self.session_data = {
            "start_time": datetime.now(timezone.utc).isoformat(),
            "events": []
        }
        self.match_id = datetime.now(timezone.utc).strftime("match_%Y%m%d_%H%M%S")

# Global match logger instance
match_logger = MatchLogger()

# Hooks for combat and game state events
def log_damage_event(attacker_id: str, target_id: str, damage: float, ability: str = None):
    match_logger.log_event("damage", {
        "attacker": attacker_id,
        "target": target_id,
        "damage": damage,
        "ability": ability
    })

def log_kill_event(killer_id: str, victim_id: str, method: str):
    match_logger.log_event("kill", {
        "killer": killer_id,
        "victim": victim_id,
        "method": method
    })

def log_objective_event(player_id: str, objective_id: str, event_type: str):
    match_logger.log_event("objective", {
        "player": player_id,
        "objective": objective_id,
        "event": event_type
    })

def log_game_state_event(state_name: str, metadata: Dict[str, Any]):
    match_logger.log_event("game_state", {
        "state": state_name,
        "metadata": metadata
    })
