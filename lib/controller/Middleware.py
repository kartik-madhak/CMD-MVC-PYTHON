from abc import ABC

from lib.communication import Request


class Middleware(ABC):
    def handle(self, request: Request):

        raise NotImplementedError
