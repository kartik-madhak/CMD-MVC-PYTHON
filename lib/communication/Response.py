import enum

from lib.view import View


class ResponseType(enum.Enum):
    valid = 0
    error = 1


class Response:
    def __init__(self, responseType: ResponseType, view: View, msg: str = ''):
        self.responseType = responseType
        self.view = view
        self.msg = msg
