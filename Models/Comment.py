import typing
from dataclasses import dataclass

from Models import User
from lib.model import Model


@dataclass
class Comment(Model):
    post_id: int
    user_id: int
    content: typing.AnyStr

    def getUserName(self):
        return User.query().select().where('id', self.user_id).getOne().name