from typing import List, Dict
from src.config.metrics.constants import ALLIANCE_MAX

class AllianceManager:
    def __init__(self):
        self.alliances: Dict[str, List[str]] = {}  # key: leader, value: list of members

    def create_alliance(self, leader: str) -> bool:
        if leader in self.alliances:
            return False
        self.alliances[leader] = [leader]
        return True

    def add_member(self, leader: str, new_member: str) -> bool:
        if leader not in self.alliances:
            return False
        if new_member in self.get_all_members():
            return False
        if len(self.alliances[leader]) >= ALLIANCE_MAX:
            return False
        self.alliances[leader].append(new_member)
        return True

    def remove_member(self, member: str):
        for leader, members in self.alliances.items():
            if member in members:
                members.remove(member)
                if leader != member and len(members) == 1:
                    del self.alliances[leader]
                return True
        return False

    def get_all_members(self) -> List[str]:
        return [p for members in self.alliances.values() for p in members]

    def get_alliances(self) -> Dict[str, List[str]]:
        return self.alliances

    def is_in_alliance(self, player: str) -> bool:
        return player in self.get_all_members()

    def detect_betrayal(self, attacker: str, target: str) -> bool:
        for members in self.alliances.values():
            if attacker in members and target in members:
                return True  # betrayal occurred
        return False

    def get_alliance_score_modifier(self, player: str) -> float:
        for members in self.alliances.values():
            if player in members:
                return 0.75  # example: alliance members earn slightly reduced score
        return 1.0
