from typing import Dict, List
from state.lobby_state import LobbyState
from state.match_timer import MatchTimer
from network.lobby import LobbyNetworkManager
from config.teams.alliance import AllianceManager


class PlayerInfo:
    def __init__(self, player_id: str, name: str):
        self.player_id = player_id
        self.name = name
        self.is_ready = False
        self.character = None
        self.perks: List[str] = []


class LobbyManager:
    def __init__(self):
        self.players: Dict[str, PlayerInfo] = {}
        self.state = LobbyState.WAITING
        self.network = LobbyNetworkManager(self)
        self.timer = MatchTimer()
        self.alliance_manager = AllianceManager()  # Alliance logic added

    def add_player(self, player_id: str, name: str):
        if player_id not in self.players:
            self.players[player_id] = PlayerInfo(player_id, name)
            self.broadcast_lobby_update()

    def remove_player(self, player_id: str):
        if player_id in self.players:
            del self.players[player_id]
            self.alliance_manager.remove_player(player_id)
            self.broadcast_lobby_update()

    def set_ready(self, player_id: str, is_ready: bool):
        if player_id in self.players:
            self.players[player_id].is_ready = is_ready
            self.check_all_ready()
            self.broadcast_lobby_update()

    def update_loadout(self, player_id: str, character: str, perks: List[str]):
        if player_id in self.players:
            self.players[player_id].character = character
            self.players[player_id].perks = perks
            self.alliance_manager.register_player_character(player_id, character)
            self.broadcast_lobby_update()

    def check_all_ready(self):
        if all(p.is_ready for p in self.players.values()) and self.players:
            self.start_countdown()

    def start_countdown(self):
        self.state = LobbyState.COUNTDOWN
        print("Countdown started!")
        self.timer.start(on_complete=self.launch_match)
        self.broadcast_lobby_update()

    def launch_match(self):
        self.state = LobbyState.LAUNCHING
        print("Launching match!")
        # Transition to game scene or start match logic here
        self.broadcast_lobby_update()

    def broadcast_lobby_update(self):
        self.network.send_lobby_state(self.players, self.state)


class LobbyScreen:
    def __init__(self, lobby_manager: LobbyManager):
        self.lobby_manager = lobby_manager
        self.local_player_id = None

    def set_local_player(self, player_id: str):
        self.local_player_id = player_id

    def toggle_ready(self):
        if self.local_player_id:
            player = self.lobby_manager.players.get(self.local_player_id)
            if player:
                new_status = not player.is_ready
                self.lobby_manager.set_ready(self.local_player_id, new_status)

    def select_loadout(self, character: str, perks: list):
        if self.local_player_id:
            self.lobby_manager.update_loadout(self.local_player_id, character, perks)

    def request_alliance(self, target_player_id: str) -> bool:
        if not self.local_player_id or self.local_player_id == target_player_id:
            return False
        return self.lobby_manager.alliance_manager.form_alliance(self.local_player_id, target_player_id)

    def break_alliance(self, target_player_id: str) -> bool:
        if not self.local_player_id or self.local_player_id == target_player_id:
            return False
        return self.lobby_manager.alliance_manager.break_alliance(self.local_player_id, target_player_id)

    def get_allies(self) -> List[str]:
        if self.local_player_id:
            return self.lobby_manager.alliance_manager.get_allies(self.local_player_id)
        return []

    def get_lobby_state(self) -> LobbyState:
        return self.lobby_manager.state

    def get_player_list(self) -> Dict[str, PlayerInfo]:
        return self.lobby_manager.players

    def get_remaining_time(self) -> int:
        if self.lobby_manager.state == LobbyState.COUNTDOWN:
            return self.lobby_manager.timer.remaining
        return 0
