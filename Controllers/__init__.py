from Controllers.UserController import *

__calledControllers = {}


def callController(name: str, method: str, request: Request):
    try:
        tmp = __calledControllers[name]
    except KeyError:
        tmp = __calledControllers[name] = globals()[name]()
    return getattr(tmp, method)(request)
