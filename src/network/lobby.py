from typing import Dict
from state.lobby_state import LobbyState
from ui.lobby_screen import PlayerInfo


class LobbyNetworkManager:
    def __init__(self, lobby_manager):
        self.lobby_manager = lobby_manager

    def handle_player_join(self, player_id: str, name: str):
        print(f"[Network] Player joined: {name} ({player_id})")
        self.lobby_manager.add_player(player_id, name)

    def handle_player_leave(self, player_id: str):
        print(f"[Network] Player left: {player_id}")
        self.lobby_manager.remove_player(player_id)

    def handle_ready_status(self, player_id: str, is_ready: bool):
        print(f"[Network] Player ready toggle: {player_id} - {is_ready}")
        self.lobby_manager.set_ready(player_id, is_ready)

    def handle_loadout_update(self, player_id: str, character: str, perks: list):
        print(f"[Network] Player loadout update: {player_id} - {character}, {perks}")
        self.lobby_manager.update_loadout(player_id, character, perks)

    def send_lobby_state(self, players: Dict[str, PlayerInfo], state: LobbyState):
        # Placeholder: serialize and broadcast lobby info to all players
        print("[Network] Broadcasting lobby state:")
        print(f"  Lobby State: {state.name}")
        for p in players.values():
            print(f"  - {p.name} | Ready: {p.is_ready} | Char: {p.character} | Perks: {p.perks}")
