from abc import ABC, abstractmethod
from typing import List

from src.base import GameObject
from src.display import Display
from src.interactions import Action, Interaction
from src.notifications import Notification, NotificationSink


class MenuItem(GameObject, ABC):
    @abstractmethod
    def select(self) -> None:
        pass

    @abstractmethod
    def focus(self) -> None:
        pass

    @abstractmethod
    def unfocus(self) -> None:
        pass


class Menu(GameObject):
    def __init__(
        self, notification_sink: NotificationSink, items: List[MenuItem]
    ) -> None:
        super().__init__(notification_sink)
        self._selected_item = 0
        self._items = items

        self._items[self._selected_item].focus()

    def _move_selection(self, movement: int) -> None:
        self._items[self._selected_item].unfocus()
        self._selected_item = (self._selected_item + movement) % len(self._items)
        self._items[self._selected_item].focus()

    def update(self, delta: float) -> None:
        self._items[self._selected_item].update(delta)

    def draw(self, display: Display) -> None:
        for item in self._items:
            item.draw(display)

    def handle_interaction(self, interaction: Interaction) -> None:
        if interaction.action == Action.MENU_UP and interaction.just_pressed:
            self._move_selection(-1)
        elif interaction.action == Action.MENU_DOWN and interaction.just_pressed:
            self._move_selection(1)
        elif interaction.action == Action.MENU_SELECT and interaction.just_pressed:
            self._items[self._selected_item].select()
        else:
            self._items[self._selected_item].handle_interaction(interaction)

    def handle_notification(self, notification: Notification) -> None:
        self._items[self._selected_item].handle_notification(notification)
