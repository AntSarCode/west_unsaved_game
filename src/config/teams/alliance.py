from typing import List, Dict, Set, Tuple
from time import time
from src.config.metrics.constants import ALLIANCE_MAX
from src.config.metrics.rules import Phase, get_character_kit

class AllianceManager:
    def __init__(self):
        # Mutual alliance map: each player points to a set of allies
        self.alliances: Dict[str, Set[str]] = {}
        self.cooldowns: Dict[Tuple[str, str], float] = {}  # (player_a, player_b): timestamp
        self.locked: bool = False
        self.current_phase: Phase = Phase.PREGAME
        self.player_characters: Dict[str, str] = {}  # player_id → character name

    def set_phase(self, phase: Phase):
        self.current_phase = phase
        self.locked = (phase == Phase.COLLAPSE)

    def register_player_character(self, player_id: str, character_name: str):
        self.player_characters[player_id] = character_name

    def is_alliance_locked_for(self, player_a: str, player_b: str) -> bool:
        if not self.locked:
            return False
        # Check if either player has special override ability
        char_a = get_character_kit(self.player_characters.get(player_a, ""))
        char_b = get_character_kit(self.player_characters.get(player_b, ""))
        if char_a and char_a.get("override_alliance_lock"):
            return False
        if char_b and char_b.get("override_alliance_lock"):
            return False
        return True

    def form_alliance(self, player_a: str, player_b: str) -> bool:
        """Attempt to form a mutual alliance between two players."""
        if player_a == player_b:
            return False

        if self.are_allied(player_a, player_b):
            return False

        now = time()
        pair = tuple(sorted((player_a, player_b)))
        if self.cooldowns.get(pair, 0) > now:
            return False

        if self.is_alliance_locked_for(player_a, player_b):
            return False

        if len(self.alliances.get(player_a, set())) >= ALLIANCE_MAX:
            return False
        if len(self.alliances.get(player_b, set())) >= ALLIANCE_MAX:
            return False

        self.alliances.setdefault(player_a, set()).add(player_b)
        self.alliances.setdefault(player_b, set()).add(player_a)
        self.cooldowns[pair] = now + 10  # 10 second cooldown
        return True

    def break_alliance(self, player_a: str, player_b: str) -> bool:
        """Break mutual alliance between two players."""
        if not self.are_allied(player_a, player_b):
            return False
        self.alliances[player_a].remove(player_b)
        self.alliances[player_b].remove(player_a)
        if not self.alliances[player_a]:
            del self.alliances[player_a]
        if not self.alliances[player_b]:
            del self.alliances[player_b]
        return True

    def remove_player(self, player: str):
        """Completely remove a player from all alliances."""
        if player in self.alliances:
            for ally in list(self.alliances[player]):
                self.alliances[ally].discard(player)
                if not self.alliances[ally]:
                    del self.alliances[ally]
            del self.alliances[player]

    def are_allied(self, player_a: str, player_b: str) -> bool:
        return player_b in self.alliances.get(player_a, set())

    def get_allies(self, player: str) -> List[str]:
        return list(self.alliances.get(player, set()))

    def get_all_members(self) -> List[str]:
        return list(self.alliances.keys())

    def detect_betrayal(self, attacker: str, target: str) -> bool:
        return self.are_allied(attacker, target)

    def get_alliance_score_modifier(self, player: str) -> float:
        if player in self.alliances:
            return 0.75  # e.g., reduced score for alliance support
        return 1.0
