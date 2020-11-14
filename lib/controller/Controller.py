from lib.controller.Middleware import Middleware


class Controller:
    def __init__(self, middleware: Middleware):
        self.middleware = middleware
