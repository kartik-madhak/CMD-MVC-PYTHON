from typing import List
from lib.event.Observer import Observer
import enum


class EventType(enum.Enum):
    info = 0
    warning = 1
    error = 2


class Event:
    observers: List[Observer]
    eventType: EventType
    message: str

    def __init__(self, eventType: EventType = EventType.info):
        self.observers = []
        self.eventType = eventType

    def addToSubscription(self, observer: Observer) -> None:
        self.observers.append(observer)

    def cancelSubscription(self, observer: Observer) -> None:
        self.observers.remove(observer)

    def notifyObservers(self) -> None:
        for observer in self.observers:
            observer.notify()
