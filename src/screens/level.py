from os import path
from typing import List

from src.constants import (
    LEVELS_FOLDER_PATH,
    WALL_CORNER_BOTTOM_LEFT,
    WALL_CORNER_BOTTOM_RIGHT,
    WALL_CORNER_TOP_LEFT,
    WALL_CORNER_TOP_RIGHT,
    WALL_HORIZONTAL,
)
from src.display import Display


def _load_level_file(level_file_path: str) -> List[str]:
    matrix = []

    with open(file=level_file_path, mode="rt", encoding="utf-8") as f:
        for line in f.readlines():
            # TODO: validate line length is correct and symbols are correct
            matrix.append(line)

    return matrix


class Level:
    def __init__(self, level_number: int) -> None:
        self._level_matrix = _load_level_file(
            level_file_path=path.join(LEVELS_FOLDER_PATH, f"{level_number:02}")
        )

    def draw(self, display: Display) -> None:
        for row in range(len(self._level_matrix)):
            for column in range(len(self._level_matrix[row])):
                character = self._level_matrix[row][column]

                if character == WALL_CORNER_TOP_LEFT:
                    # TODO: draw top left wall image
                    return
                elif character == WALL_CORNER_TOP_RIGHT:
                    # TODO: draw top right wall image
                    return
                elif character == WALL_CORNER_BOTTOM_LEFT:
                    # TODO: draw bottom left wall image
                    return
                elif character == WALL_CORNER_BOTTOM_RIGHT:
                    # TODO: draw bottom right wall image
                    return
                elif character == WALL_HORIZONTAL:
                    # TODO: draw horizontal wall
                    return
