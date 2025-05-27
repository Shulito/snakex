from os import path

from src.constants import SCREENS_FOLDER_PATH
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink
from src.screens.base import GameScreen


class GameArenaGameScreen(GameScreen):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(
            notification_sink=notification_sink,
            background_sprite_file_path=path.join(
                SCREENS_FOLDER_PATH, "studio_logo.png"
            ),
        )

    def update(self, delta: float) -> None:
        pass

    def handle_interaction(self, interaction: Interaction) -> None:
        pass

    def handle_notification(self, notification: Notification) -> None:
        pass
