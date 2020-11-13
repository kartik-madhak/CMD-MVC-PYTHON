from typing import List
from lib.event.Observer import Observer
import enum


class EventType(enum.Enum):
    info = 0
    warning = 1
    error = 2


class Event:
    def __init__(self, eventType: EventType = EventType.info, message: str = 'logged successfully'):
        self.eventType = eventType
        self.message = message

    def __str__(self) -> str:
        return 'Event Type: ' + self.eventType.name + ', Message: ' + self.message


class EventHandler:
    __observers: List[Observer]

    def __init__(self):
        self.__observers = []

    def dispatch(self, event: Event) -> None:
        for observer in self.__observers:
            observer.notify(event)

    def addToSubscription(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def cancelSubscription(self, observer: Observer) -> None:
        self.__observers.remove(observer)
