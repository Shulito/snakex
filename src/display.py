import os

import pygame

from src.constants import (
    DISPLAY_BACKGROUND_COLOR,
    DISPLAY_RESOLUTION,
    GAME_TITLE,
    SDL_VIDEO_CENTERED_ENV_VAR,
    SDL_VIDEO_CENTERED_TRUE,
)


class Display:
    def __init__(self) -> None:
        pygame.display.set_caption(GAME_TITLE)
        os.environ[SDL_VIDEO_CENTERED_ENV_VAR] = SDL_VIDEO_CENTERED_TRUE

        self._display = pygame.display.set_mode(DISPLAY_RESOLUTION)

    def update(self) -> None:
        self._display.fill(DISPLAY_BACKGROUND_COLOR)
        pygame.display.flip()

    def draw(self, sprite: pygame.sprite.Sprite) -> None:
        self._display.blit(sprite.image, sprite.rect)  # type: ignore
