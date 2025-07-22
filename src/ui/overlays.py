from ursina import Text, color, destroy
import time

class OverlayManager:
    def __init__(self):
        self.pause_overlay = Text(
            text='[ PAUSED ]',
            origin=(0, 0),
            position=(0, 0.1),
            scale=2,
            color=color.gray,
            background=True
        )
        self.pause_overlay.enabled = False

        self.phase_overlay = Text(
            text='',
            origin=(0, 0),
            position=(0, 0.3),
            scale=1.5,
            color=color.cyan,
            background=True
        )
        self.phase_overlay.enabled = False

        self.alliance_overlay = Text(
            text='',
            origin=(0, 0),
            position=(0, -0.35),
            scale=1.25,
            color=color.lime,
            background=True
        )
        self.alliance_overlay.enabled = False
        self.alliance_timer = 0

        self.betrayal_overlay = Text(
            text='',
            origin=(0, 0),
            position=(0, -0.45),
            scale=1.25,
            color=color.red,
            background=True
        )
        self.betrayal_overlay.enabled = False
        self.betrayal_timer = 0

        self.kill_feed = []
        self.max_kill_feed = 5

    def toggle_pause(self, is_paused: bool):
        self.pause_overlay.enabled = is_paused

    def show_phase_transition(self, phase_name: str, color_hint=color.cyan):
        self.phase_overlay.text = f'Phase: {phase_name}'
        self.phase_overlay.color = color_hint
        self.phase_overlay.enabled = True

    def hide_phase_transition(self):
        self.phase_overlay.enabled = False

    def show_alliance_formation(self, members: list):
        names = ', '.join(members)
        self.alliance_overlay.text = f'Alliance Formed: {names}'
        self.alliance_overlay.enabled = True
        self.alliance_timer = time.time()

    def hide_alliance_overlay(self):
        self.alliance_overlay.enabled = False

    def show_betrayal(self, betrayer: str, target: str):
        self.betrayal_overlay.text = f'{betrayer} betrayed {target}!'
        self.betrayal_overlay.enabled = True
        self.betrayal_timer = time.time()

    def hide_betrayal_overlay(self):
        self.betrayal_overlay.enabled = False

    def update_overlays(self):
        now = time.time()
        if self.alliance_overlay.enabled and now - self.alliance_timer > 4:
            self.hide_alliance_overlay()
        if self.betrayal_overlay.enabled and now - self.betrayal_timer > 4:
            self.hide_betrayal_overlay()

    def add_kill_feed(self, killer_name: str, victim_name: str, weapon_name: str = None):
        skull = "\U0001F480"
        text = f"{killer_name} {skull} {victim_name}"
        if weapon_name:
            text += f" [{weapon_name}]"
        entry = Text(
            text=text,
            position=(0.65, 0.4 - len(self.kill_feed)*0.05),
            scale=1.1,
            color=color.white,
            origin=(0, 0)
        )
        self.kill_feed.insert(0, entry)

        if len(self.kill_feed) > self.max_kill_feed:
            removed = self.kill_feed.pop()
            destroy(removed)

    def update_kill_feed_positions(self):
        for i, entry in enumerate(self.kill_feed):
            entry.y = 0.4 - i * 0.05
