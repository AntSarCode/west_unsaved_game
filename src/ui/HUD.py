from ursina import Entity, Text, color
from typing import List

class HUD:
    def __init__(self):
        self.score_text = Text(
            text='Score: 0',
            position=(-0.85, 0.45),
            scale=1.25,
            color=color.white,
            background=True
        )

        self.event_log: List[str] = []
        self.event_text = Text(
            text='',
            position=(-0.85, 0.35),
            scale=0.9,
            color=color.azure,
            background=True
        )

        self.health_bar = Entity(
            model='quad',
            color=color.red,
            position=(-0.85, 0.55),
            scale=(0.3, 0.025)
        )

        self.status_effect_text = Text(
            text='',
            position=(-0.85, 0.25),
            scale=0.8,
            color=color.lime,
            background=True
        )

        self.ammo_text = Text(
            text='',
            position=(-0.85, 0.2),
            scale=0.9,
            color=color.yellow,
            background=True
        )

        self.weapon_text = Text(
            text='',
            position=(-0.85, 0.15),
            scale=0.8,
            color=color.orange,
            background=True
        )

    def update_score(self, new_score: int):
        self.score_text.text = f'Score: {new_score}'

    def log_event(self, message: str):
        if len(self.event_log) >= 5:
            self.event_log.pop(0)
        self.event_log.append(message)
        self.event_text.text = '\n'.join(self.event_log)

    def update_health(self, current: int, max_hp: int):
        percent = max(0.0, min(1.0, current / max_hp))
        self.health_bar.scale_x = 0.3 * percent

    def update_ammo(self, current: int, capacity: int, reserve: int):
        self.ammo_text.text = f'Ammo: {current}/{capacity} ({reserve})'

    def update_weapon_name(self, name: str):
        self.weapon_text.text = f'Weapon: {name}'

    def show_status_effects(self, active_effects: List[str]):
        self.status_effect_text.text = ' / '.join(active_effects)

    def hide(self):
        self.score_text.enabled = False
        self.event_text.enabled = False
        self.health_bar.enabled = False
        self.status_effect_text.enabled = False
        self.ammo_text.enabled = False
        self.weapon_text.enabled = False

    def show(self):
        self.score_text.enabled = True
        self.event_text.enabled = True
        self.health_bar.enabled = True
        self.status_effect_text.enabled = True
        self.ammo_text.enabled = True
        self.weapon_text.enabled = True
