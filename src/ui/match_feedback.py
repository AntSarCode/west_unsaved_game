from ursina import Text, color, destroy
from time import time as system_time
from config.teams.alliance import AllianceManager

class MatchFeedback:
    def __init__(self):
        self.feedback_elements = []
        self.alliance_manager: AllianceManager = None

    def set_alliance_manager(self, manager: AllianceManager):
        self.alliance_manager = manager

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

    def show_alliance_summary(self):
        if not self.alliance_manager:
            return

        survivors = self.alliance_manager.get_all_members()
        if not survivors:
            self.show_feedback("No alliances survived.", duration=3.5, color_hint=color.gray)
            return

        for player_id in survivors:
            allies = self.alliance_manager.get_allies(player_id)
            if allies:
                self.show_feedback(f"{player_id} survived with {', '.join(allies)}", duration=3.5, color_hint=color.azure)
            else:
                self.show_feedback(f"{player_id} survived solo.", duration=3.5, color_hint=color.orange)

    def update(self):
        now = system_time()
        remaining_elements = []
        for item in self.feedback_elements:
            if now >= item["expires_at"]:
                destroy(item["text"])
            else:
                remaining_elements.append(item)
        self.feedback_elements = remaining_elements
