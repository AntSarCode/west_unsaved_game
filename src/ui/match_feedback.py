from ursina import Text, color, destroy
from time import time as system_time

class MatchFeedback:
    def __init__(self):
        self.feedback_elements = []

    def show_feedback(self, message: str, duration: float = 2.5, color_hint=color.yellow):
        timestamp = system_time()
        feedback_text = Text(
            text=message,
            position=(0, 0.3),
            origin=(0, 0),
            scale=1.5,
            color=color_hint,
            background=True
        )
        self.feedback_elements.append({
            "text": feedback_text,
            "expires_at": timestamp + duration
        })

    def update(self):
        now = system_time()
        remaining_elements = []
        for item in self.feedback_elements:
            if now >= item["expires_at"]:
                destroy(item["text"])
            else:
                remaining_elements.append(item)
        self.feedback_elements = remaining_elements
