import typing
from dataclasses import dataclass
from datetime import datetime

from lib.model import Model


@dataclass
class User(Model):
    id: int
    name: str
    email: str
    description: typing.AnyStr
    passwordHash: str
    permissionLevel: int
    created_at: datetime
    updated_at: datetime

    def __hash__(self):
        return hash(self.__dict__.values())

