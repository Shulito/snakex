from src.base import GameObject
from src.constants import (
    CREDITS_SCREEN_NAME,
    EXTRA_DATA_SCREEN_NAME,
    GAME_ARENA_SCREEN_NAME,
    GAME_OVER_SCREEN_NAME,
    MAIN_MENU_SCREEN_NAME,
    OPTIONS_MENU_SCREEN_NAME,
    STUDIO_LOGO_SCREEN_NAME,
    WIN_SCREEN_NAME,
)
from src.display import Display
from src.interactions import Interaction
from src.notifications import Notification, NotificationSink, NotificationType
from src.screens.base import GameScreen
from src.screens.credits import CreditsGameScreen
from src.screens.game_arena import GameArenaGameScreen
from src.screens.game_over import GameOverGameScreen
from src.screens.options_menu import OptionsMenuGameScreen
from src.screens.studio_logo import StudioLogoGameScreen
from src.screens.win import WinGameScreen


class ScreenManager(GameObject):
    def __init__(self, notification_sink: NotificationSink) -> None:
        super().__init__(notification_sink)

        self._game_screen: GameScreen = None  # type: ignore
        self._change_screen(STUDIO_LOGO_SCREEN_NAME)

    def _change_screen(self, screen_name: str) -> None:
        if screen_name == STUDIO_LOGO_SCREEN_NAME:
            self._game_screen = StudioLogoGameScreen(
                notification_sink=self._notification_sink
            )
        elif screen_name == MAIN_MENU_SCREEN_NAME:
            self._game_screen = StudioLogoGameScreen(
                notification_sink=self._notification_sink
            )
        elif screen_name == OPTIONS_MENU_SCREEN_NAME:
            self._game_screen = OptionsMenuGameScreen(
                notification_sink=self._notification_sink
            )
        elif screen_name == CREDITS_SCREEN_NAME:
            self._game_screen = CreditsGameScreen(
                notification_sink=self._notification_sink
            )
        elif screen_name == GAME_ARENA_SCREEN_NAME:
            self._game_screen = GameArenaGameScreen(
                notification_sink=self._notification_sink
            )
        elif screen_name == WIN_SCREEN_NAME:
            self._game_screen = WinGameScreen(notification_sink=self._notification_sink)
        elif screen_name == GAME_OVER_SCREEN_NAME:
            self._game_screen = GameOverGameScreen(
                notification_sink=self._notification_sink
            )
        else:
            raise ValueError(f"{screen_name} is not a recognizable screen name")

    def draw(self, display: Display) -> None:
        self._game_screen.draw(display)

    def handle_interaction(self, interaction: Interaction) -> None:
        self._game_screen.handle_interaction(interaction)

    def update(self, delta: float) -> None:
        self._game_screen.update(delta)

    def handle_notification(self, notification: Notification) -> None:
        if notification.type == NotificationType.CHANGE_SCREEN:
            self._change_screen(notification.extra_data[EXTRA_DATA_SCREEN_NAME])
        else:
            self._game_screen.handle_notification(notification)
