from abc import ABC

from lib.communication import Request


class Middleware(ABC):
    def __init__(self, name):
        self.name = name

    def handle(self, request: Request):
        raise NotImplementedError
