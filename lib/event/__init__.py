from lib.event.Event import *

__EventHandlerInstance = None


def getEventHandler() -> EventHandler:
    global __EventHandlerInstance
    # print(__EventHandlerInstance)
    if __EventHandlerInstance is None:
        __EventHandlerInstance = EventHandler()
    return __EventHandlerInstance
