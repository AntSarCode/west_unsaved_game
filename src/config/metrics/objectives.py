from ursina import Entity, color, distance, time
from config.metrics.constants import CAPTURE_TIME, CAPTURE_RADIUS, CAPTURE_POINTS
from config.metrics.rules import Phase
from ui.overlays import OverlayManager

class ObjectiveBase:
    def __init__(self, name: str, point_value: int):
        self.name = name
        self.point_value = point_value
        self.completed_by = None
        self.is_complete = False

    def complete(self, player):
        self.completed_by = player.name
        self.is_complete = True
        player.score += self.point_value
        if hasattr(player, 'match_feedback'):
            player.match_feedback.show_feedback(f"{player.name} completed {self.name} for {self.point_value} points!", color_hint=color.green)


class CapturePoint(ObjectiveBase, Entity):
    def __init__(self, name, position=(0, 0, 5)):
        ObjectiveBase.__init__(self, name, CAPTURE_POINTS)
        Entity.__init__(
            self,
            model='cube',
            color=color.azure,
            position=position,
            scale=(2, 0.2, 2)
        )
        self.owner = None
        self.capture_time = 0
        self.contested = False

    def update(self, players, current_phase: Phase = Phase.SPAWN, overlay: OverlayManager = None):
        if self.is_complete:
            return

        if current_phase != Phase.OBJECTIVE_GATHERING:
            return  # Only capturable in objective phase

        nearby = [p for p in players if distance(p.position, self.position) <= CAPTURE_RADIUS]

        if nearby:
            capturers = list(set(p.team for p in nearby if hasattr(p, 'team')))
            if len(capturers) > 1:
                self.contested = True
                return

            self.contested = False
            self.capture_time += getattr(time, 'dt', 0)

            if self.capture_time >= CAPTURE_TIME:
                self.owner = capturers[0] if capturers else nearby[0].name
                for p in nearby:
                    p.score += CAPTURE_POINTS // len(nearby)
                self.complete(nearby[0])
                print(f'{self.owner} captured {self.name} for {self.point_value} points!')
                if overlay:
                    overlay.show_phase_transition(f"{self.name} Captured!", color.green)
        else:
            self.capture_time = 0
            self.contested = False


class BossKillObjective(ObjectiveBase):
    def __init__(self, name: str, boss_entity, point_value: int):
        super().__init__(name, point_value)
        self.boss = boss_entity

    def check_defeat(self, overlay: OverlayManager = None):
        if self.boss.health <= 0 and not self.is_complete:
            killer = self.boss.last_damager
            self.complete(killer)
            print(f'{killer.name} killed {self.boss.name} for {self.point_value} points.')
            if overlay:
                overlay.show_phase_transition(f"{self.boss.name} Defeated!", color.red)


class LootRaceObjective(ObjectiveBase):
    def __init__(self, name: str, finish_trigger, point_value: int):
        super().__init__(name, point_value)
        self.finish_trigger = finish_trigger  # Trigger zone or interaction

    def check_completion(self, player, overlay: OverlayManager = None):
        if not self.is_complete and self.finish_trigger.triggered_by(player):
            self.complete(player)
            print(f'{player.name} completed loot race {self.name}!')
            if overlay:
                overlay.show_phase_transition(f"{player.name} won {self.name}!", color.violet)
