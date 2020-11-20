import enum
from typing import TypedDict

from lib.view import View


class ResponseType(enum.Enum):
    valid = 0
    error = 1


class Response:
    def __init__(self, responseType: ResponseType, view: View):
        self.responseType = responseType
        self.view = view
