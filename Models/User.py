import hashlib
import typing
from dataclasses import dataclass
from datetime import datetime

from lib.model import Model


@dataclass
class User(Model):
    name: str
    email: str
    description: typing.AnyStr
    passwordHash: str
    role: int

    def hash(self):
        md5 = hashlib.md5()
        md5.update(repr(self).encode())
        return md5.hexdigest()

