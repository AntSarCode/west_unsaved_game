from ursina import Entity, color, distance, time
from src.config.metrics.constants import CAPTURE_TIME, CAPTURE_RADIUS, CAPTURE_POINTS

class CapturePoint(Entity):
    def __init__(self, name, position=(0, 0, 5)):
        super().__init__(
            model='cube',
            color=color.azure,
            position=position,
            scale=(2, 0.2, 2)
        )
        self.name = name
        self.owner = None
        self.capture_time = 0
        self.is_captured = False
        self.contested = False

    def update(self, players):
        if self.is_captured:
            return  # Already claimed

        nearby = [p for p in players if distance(p.position, self.position) <= CAPTURE_RADIUS]

        if nearby:
            capturers = list(set(p.team for p in nearby if hasattr(p, 'team')))
            if len(capturers) > 1:
                self.contested = True
                return
            self.contested = False # inline import avoids type check error
            self.capture_time += getattr(time, 'dt', 0)
            if self.capture_time >= CAPTURE_TIME:
                self.owner = capturers[0] if capturers else nearby[0].name
                for p in nearby:
                    p.score += CAPTURE_POINTS // len(nearby)
                self.is_captured = True
                print(f'{self.owner} captured {self.name} for {CAPTURE_POINTS} points!')
        else:
            self.capture_time = 0
            self.contested = False
