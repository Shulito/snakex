from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List


class NotificationType(Enum):
    CHANGE_SCREEN = 0


@dataclass(frozen=True)
class Notification:
    type: NotificationType
    extra_data: Dict[str, Any]


class NotificationSink:
    def __init__(self) -> None:
        self._notifications: List[Notification] = []

    def add(self, notification: Notification) -> None:
        self._notifications.append(notification)

    def read_all(self) -> List[Notification]:
        result = self._notifications.copy()
        self._notifications.clear()

        return result
