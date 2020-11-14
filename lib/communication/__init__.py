from lib.communication.Request import *
from lib.communication.Response import *
from lib.communication.Router import *

from Routes.routes import getRoutes

__RouterInstance = None


def getRouter() -> Router:
    global __RouterInstance
    if __RouterInstance is None:
        __RouterInstance = Router(getRoutes())
    return __RouterInstance
