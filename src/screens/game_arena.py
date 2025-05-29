from os import path

from src.constants import SCREENS_FOLDER_PATH
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink
from src.screens.base import GameScreen
from src.screens.level import Level


class GameArenaGameScreen(GameScreen):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(
            notification_sink=notification_sink,
            background_sprite_file_path=path.join(
                SCREENS_FOLDER_PATH, "studio_logo.png"
            ),
        )

        self._level = Level(level_number=1)

    def draw(self, display: Display) -> None:
        super().draw(display)
        self._level.draw(display)

    def update(self, delta: float) -> None:
        pass

    def handle_interaction(self, interaction: Interaction) -> None:
        pass

    def handle_notification(self, notification: Notification) -> None:
        pass
