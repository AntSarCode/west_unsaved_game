from enum import Enum, auto
from dataclasses import dataclass, field
from typing import List, Optional
from users.status_effects import status_effect_types
from users.characters import character_kits, NICKNAME_INDEX

# --- ENUM DEFINITIONS ---

class Phase(Enum):
    PREGAME = auto()
    SPAWN = auto()
    OBJECTIVE_GATHERING = auto()
    COLLAPSE = auto()
    SHOWDOWN = auto()

class StatusEffect(Enum):
    BLEED = auto()
    STUN = auto()
    SLOW = auto()
    MARK = auto()
    BURN = auto()
    FREEZE = auto()
    POISON = auto()
    STEALTH = auto()
    FEAR = auto()
    ALLURE = auto()

# --- DATACLASS DEFINITIONS ---

@dataclass
class Player:
    name: str
    character: str
    perk: Optional[str] = None
    alliance_id: Optional[int] = None
    economy: int = 1500
    effects: List[StatusEffect] = field(default_factory=list)
    is_alive: bool = True
    respawn_time: int = 0

    def forgo_perk(self):
        if self.perk is None:
            self.economy += 400

@dataclass
class Objective:
    name: str
    point_value: int
    completed_by: Optional[str] = None

@dataclass
class Alliance:
    id: int
    members: List[str]
    locked: bool = False

# --- PHASE MANAGEMENT ---

# noinspection PyMethodMayBeStatic
class Game:
    def __init__(self):
        self.players: List[Player] = []
        self.alliances: List[Alliance] = []
        self.phase: Phase = Phase.PREGAME
        self.time_in_phase: int = 0  # in seconds

    def next_phase(self):
        phase_order = list(Phase)
        current_index = phase_order.index(self.phase)
        if current_index + 1 < len(phase_order):
            self.phase = phase_order[current_index + 1]
            self.time_in_phase = 0

    def update_respawns(self):
        for player in self.players:
            if not player.is_alive and player.respawn_time > 0:
                player.respawn_time -= 1
                if player.respawn_time == 0:
                    player.is_alive = True
                    print(f"{player.name} has respawned.")

    def assign_status(self, player: Player, effect: StatusEffect):
        if effect not in player.effects:
            player.effects.append(effect)

# --- ECONOMY SYSTEM ---

class Economy:
    @staticmethod
    def reward_kill(streak: int) -> int:
        return min(400, 250 + streak * 25)

    @staticmethod
    def reward_objective(complexity: int) -> int:
        return min(1500, 500 + complexity * 200)

    @staticmethod
    def reward_loot(crate_quality: float) -> int:
        return int(200 + (crate_quality * 800))

# --- STATUS EFFECTS LOGIC MAP ---

def apply_effect(player: Player, effect_name: str):
    if effect_name in status_effect_types:
        effect_enum = StatusEffect[effect_name.upper()]
        game.assign_status(player, effect_enum)

# --- CHARACTER DEFINITIONS ---

def get_character_kit(name: str) -> Optional[dict]:
    """
    Resolves full character kit from character name or nickname.
    Returns the ability/kit dict or None if not found.
    """
    # Resolve nickname to full name if needed
    full_name = NICKNAME_INDEX.get(name, name)
    return character_kits.get(full_name)

# --- FULL INITIALIZATION  ---

if __name__ == "__main__":
    game = Game()

    # Add full characters using nickname and full name support
    character_names = ["Clogade", "Mama B", "Frosty", "Princess", "Trey Card"]
    for name in character_names:
        kit = get_character_kit(name)
        if kit:
            game.players.append(Player(name=name, character=name))

    # Forgo perks in pregame
    for p in game.players:
        p.forgo_perk()

    # Advance to SPAWN phase
    game.next_phase()
    print(f"Phase is now {game.phase.name}")

    # Apply a sample status effect
    apply_effect(game.players[0], "fear")
    print(f"{game.players[0].name} effects: {game.players[0].effects}")

