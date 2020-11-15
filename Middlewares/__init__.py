from lib.communication import Request
from Middlewares.AuthMiddleware import AuthMiddleware

__calledMiddleware = {}


def callMiddleware(name: str, method: str, request: Request):
    try:
        tmp = __calledMiddleware[name]
    except KeyError:
        tmp = __calledMiddleware[name] = globals()[name]()
    return getattr(tmp, method)(request)
