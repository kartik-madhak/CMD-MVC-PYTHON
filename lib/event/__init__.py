from lib.event.Event import *

__EventHandlerInstance = None


def getEventHandler() -> EventHandler:
    global __EventHandlerInstance
    # print(__EventHandlerInstance)
    if __EventHandlerInstance is None:
        print('Came here')
        __EventHandlerInstance = EventHandler()
    print('Came here twice')
    return __EventHandlerInstance
