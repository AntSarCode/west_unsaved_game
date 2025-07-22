import time
import threading
from typing import Callable


class MatchTimer:
    def __init__(self, duration: int = 30):
        self.duration = duration
        self.remaining = duration
        self.running = False
        self.on_complete: Callable[[], None] = lambda: None
        self._thread = None

    def start(self, on_complete: Callable[[], None] = None):
        if on_complete:
            self.on_complete = on_complete
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._run_timer)
            self._thread.start()

    def _run_timer(self):
        print(f"[Timer] Countdown started: {self.duration} seconds")
        while self.remaining > 0 and self.running:
            print(f"[Timer] {self.remaining} seconds remaining...")
            time.sleep(1)
            self.remaining -= 1
        if self.running:
            print("[Timer] Countdown complete!")
            self.on_complete()
        self.running = False

    def cancel(self):
        self.running = False
        self.remaining = self.duration
        print("[Timer] Countdown cancelled.")
