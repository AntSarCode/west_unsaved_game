from ursina import Text, color
from time import time

class DebugOverlay:
    def __init__(self):
        self.enabled = False
        self.text_entity = Text(
            text='[Debug Info]',
            position=(-0.85, 0.45),
            origin=(0,0),
            scale=0.9,
            background=True,
            color=color.azure,
            enabled=False
        )
        self.start_time = time()
        self.fps_counter = 0
        self.last_fps_time = self.start_time

        self.state_data = {
            'FPS': 0,
            'Elapsed': 0,
            'Players': 0,
            'Phase': 'Unknown'
        }

    def toggle(self):
        self.enabled = not self.enabled
        self.text_entity.enabled = self.enabled

    def update(self, players: int, phase: str):
        if not self.enabled:
            return

        self.fps_counter += 1
        current_time = time()
        elapsed = current_time - self.last_fps_time
        total_elapsed = current_time - self.start_time

        if elapsed >= 1.0:
            self.state_data['FPS'] = self.fps_counter
            self.state_data['Elapsed'] = int(total_elapsed)
            self.state_data['Players'] = players
            self.state_data['Phase'] = phase

            self.text_entity.text = '\n'.join([
                f"{key}: {value}" for key, value in self.state_data.items()
            ])
            self.fps_counter = 0
            self.last_fps_time = current_time
