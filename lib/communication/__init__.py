from lib.communication.request import *
from lib.communication.router import *

__RouterInstance = None


def getRouter() -> Router:
    global __RouterInstance
    if __RouterInstance is None:
        __RouterInstance = Router()
    return __RouterInstance