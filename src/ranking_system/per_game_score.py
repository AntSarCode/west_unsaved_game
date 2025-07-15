from src.config.metrics.constants import (
    SOLO_KILL_POINTS,
    SOLO_ASSIST_POINTS,
    ALLIANCE_KILL_POINTS,
    ALLIANCE_ASSIST_POINTS,
    CAPTURE_POINTS,
    BOSS_KILL_POINTS
)

from src.config.teams.alliance import AllianceManager

class ScoreTracker:
    def __init__(self):
        self.scores = {}
        self.alliance_manager = AllianceManager()

    def add_player(self, player: str):
        if player not in self.scores:
            self.scores[player] = 0

    def award_kill(self, attacker: str, target: str):
        is_betrayal = self.alliance_manager.detect_betrayal(attacker, target)
        modifier = self.alliance_manager.get_alliance_score_modifier(attacker)
        points = SOLO_KILL_POINTS if modifier == 1.0 else ALLIANCE_KILL_POINTS
        if is_betrayal:
            points = points * 0.25  # heavy penalty for betrayal
        self._add_points(attacker, points)

    def award_assist(self, assister: str):
        modifier = self.alliance_manager.get_alliance_score_modifier(assister)
        points = SOLO_ASSIST_POINTS if modifier == 1.0 else ALLIANCE_ASSIST_POINTS
        self._add_points(assister, points)

    def award_capture(self, capturing_team: list):
        per_player_points = CAPTURE_POINTS / len(capturing_team)
        for player in capturing_team:
            self._add_points(player, per_player_points)

    def award_boss_kill(self, team: list):
        per_player_points = BOSS_KILL_POINTS / len(team)
        for player in team:
            self._add_points(player, per_player_points)

    def _add_points(self, player: str, points: float):
        self.add_player(player)
        self.scores[player] += points

    def get_score(self, player: str) -> float:
        return self.scores.get(player, 0)

    def get_leaderboard(self) -> dict:
        return dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True))
