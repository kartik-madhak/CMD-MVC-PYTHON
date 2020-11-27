import typing
from dataclasses import dataclass

from lib.model import Model


@dataclass
class Notification(Model):
    user_id: int
    content: typing.AnyStr
    is_read: int
