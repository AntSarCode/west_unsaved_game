from enum import Enum

class LobbyState(Enum):
    WAITING = 1
    READY = 2
    COUNTDOWN = 3
    LAUNCHING = 4
