from enum import Enum, auto

class Phase(Enum):
    PREGAME = auto()
    SPAWN = auto()
    OBJECTIVE = auto()
    COLLAPSE = auto()
    SHOWDOWN = auto()

PHASE_TIMINGS = {
    Phase.PREGAME: 120,      # 90–120 sec, maxed here
    Phase.SPAWN: 15,         # 10–15 sec
    Phase.OBJECTIVE: 1200,   # Max 20 minutes
    Phase.COLLAPSE: 600,     # Max 10 minutes
    Phase.SHOWDOWN: None,    # Until finished
}

PHASE_DESCRIPTIONS = {
    Phase.PREGAME: "Character and perk selection. Starting economy granted.",
    Phase.SPAWN: "Players spawn with invincibility buffer.",
    Phase.OBJECTIVE: "Players attempt dynamic objectives and resource gathering.",
    Phase.COLLAPSE: "Map shrinks periodically, forcing encounters.",
    Phase.SHOWDOWN: "Final confrontation. Respawns disabled. Winner decided.",
}

class PhaseState:
    def __init__(self):
        self.current_phase = Phase.PREGAME
        self.time_remaining = PHASE_TIMINGS[self.current_phase]

    def advance_phase(self):
        if self.current_phase == Phase.PREGAME:
            self.current_phase = Phase.SPAWN
        elif self.current_phase == Phase.SPAWN:
            self.current_phase = Phase.OBJECTIVE
        elif self.current_phase == Phase.OBJECTIVE:
            self.current_phase = Phase.COLLAPSE
        elif self.current_phase == Phase.COLLAPSE:
            self.current_phase = Phase.SHOWDOWN
        else:
            return  # Game complete

        self.time_remaining = PHASE_TIMINGS[self.current_phase]
        print(f"Phase advanced to: {self.current_phase.name}")

    def tick(self, seconds=1):
        if self.time_remaining is not None:
            self.time_remaining -= seconds
            if self.time_remaining <= 0:
                self.advance_phase()

    def describe_current_phase(self):
        return PHASE_DESCRIPTIONS[self.current_phase]
