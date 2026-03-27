from enum import Enum, auto
from typing import Any, Callable, Dict, List


class MazeEvent(Enum):
    MAZE_GENERATED = auto()
    MAZE_STEP = auto()
    SOLVE_COMPLETE = auto()
    SOLVE_STEP = auto()
    TYPE_CHANGED = auto()
    ERROR = auto()


EventCallback = Callable[..., None]


class EventBus:
    """Bus d'événements typés pour la communication MVC (Contrôleur → Vues)."""

    def __init__(self) -> None:
        self._listeners: Dict[MazeEvent, List[EventCallback]] = {}

    def subscribe(self, event: MazeEvent, callback: EventCallback) -> None:
        self._listeners.setdefault(event, []).append(callback)

    def unsubscribe(self, event: MazeEvent, callback: EventCallback) -> None:
        if event in self._listeners:
            try:
                self._listeners[event].remove(callback)
            except ValueError:
                pass

    def emit(self, event: MazeEvent, **kwargs: Any) -> None:
        for cb in list(self._listeners.get(event, [])):
            cb(**kwargs)
