import time

class GameClock:
    def __init__(self, tick_rate=1.0):
        self.tick_rate = tick_rate  # seconds per tick
        self.last_tick_time = time.time()
        self.subscribers = []  # List of (callable, interval)

    def subscribe(self, func, interval=1):
        self.subscribers.append({
            'func': func,
            'interval': interval,
            'next_call': time.time() + interval
        })

    def run_tick(self):
        now = time.time()
        for sub in self.subscribers:
            if now >= sub['next_call']:
                sub['func']()
                sub['next_call'] = now + sub['interval']
        self.last_tick_time = now

    def run_forever(self):
        while True:
            self.run_tick()
            time.sleep(self.tick_rate)
