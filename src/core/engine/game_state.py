from src.config.metrics.constants import (
    ALLIANCE_MAX,
    SOLO_KILL_POINTS,
    SOLO_ASSIST_POINTS,
    ALLIANCE_KILL_POINTS,
    ALLIANCE_ASSIST_POINTS,
    CAPTURE_RADIUS
)

class GameState:
    def __init__(self):
        self.players = {}
        self.alliances = []
        self.active_objectives = []
        self.dead_players = []
        self.phase_state = None  # Can be linked to PhaseState instance

    def add_player(self, player):
        self.players[player.name] = player

    def remove_player(self, player):
        self.players.pop(player.name, None)
        self.dead_players.append(player)

    def create_alliance(self, p1, p2):
        if len(self.alliances) < ALLIANCE_MAX:
            self.alliances.append({'members': [p1, p2]})

    def terminate_alliance(self, p1, p2):
        for alliance in self.alliances:
            if set(alliance['members']) == {p1, p2}:
                self.alliances.remove(alliance)
                break

    def award_kill_points(self, player, in_alliance=False):
        if in_alliance:
            player.score += ALLIANCE_KILL_POINTS
        else:
            player.score += SOLO_KILL_POINTS

    def award_assist_points(self, player, in_alliance=False):
        if in_alliance:
            player.score += ALLIANCE_ASSIST_POINTS
        else:
            player.score += SOLO_ASSIST_POINTS

    def get_nearby_players(self, player, radius=CAPTURE_RADIUS):
        # Placeholder spatial logic, assumes player.position exists
        return [p for p in self.players.values()
                if p.name != player.name and hasattr(p, 'position') and player.position.distance_to(p.position) <= radius]

    def apply_team_buff(self, player, buff_type, value, duration):
        # Placeholder for buff logic (e.g., damage boost to allies)
        for alliance in self.alliances:
            if player in alliance['members']:
                for ally in alliance['members']:
                    if ally != player:
                        ally.apply_buff(buff_type, value, duration)
