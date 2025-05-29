from os import path
from typing import Final, Tuple

# General constants
GAME_TITLE: Final[str] = "Snake X"
FPS: Final[int] = 60

BACKGROUND_TOP_LEFT_COORD: Final[Tuple[int, int]] = (0, 0)

# Display constants
DISPLAY_RESOLUTION: Final[Tuple[int, int]] = (800, 600)
DISPLAY_BACKGROUND_COLOR: Final[Tuple[int, int, int]] = (0, 0, 0)

SDL_VIDEO_CENTERED_ENV_VAR: Final[str] = "SDL_VIDEO_CENTERED"
SDL_VIDEO_CENTERED_TRUE: Final[str] = "1"

# Screen constants
STUDIO_LOGO_SCREEN_NAME: Final[str] = "STUDIO_LOGO"
MAIN_MENU_SCREEN_NAME: Final[str] = "MAIN_MENU"
OPTIONS_MENU_SCREEN_NAME: Final[str] = "OPTIONS_MENU"
CREDITS_SCREEN_NAME: Final[str] = "CREDITS"
GAME_ARENA_SCREEN_NAME: Final[str] = "GAME_ARENA"
WIN_SCREEN_NAME: Final[str] = "WIN"
GAME_OVER_SCREEN_NAME: Final[str] = "GAME_OVER"

# Notification constants
EXTRA_DATA_SCREEN_NAME: Final[str] = "SCREEN_NAME"

# Level constants
WALL_CORNER_TOP_LEFT: Final[str] = "╔"
WALL_CORNER_TOP_RIGHT: Final[str] = "╗"
WALL_CORNER_BOTTOM_LEFT: Final[str] = "╚"
WALL_CORNER_BOTTOM_RIGHT: Final[str] = "╝"
WALL_HORIZONTAL: Final[str] = "═"

# Assets constants
ASSETS_FOLDER_PATH: Final[str] = path.abspath(
    path.join(path.dirname(__file__), "..", "assets")
)

SCREENS_FOLDER_PATH: Final[str] = path.join(ASSETS_FOLDER_PATH, "screens")
LEVELS_FOLDER_PATH: Final[str] = path.join(ASSETS_FOLDER_PATH, "levels")
