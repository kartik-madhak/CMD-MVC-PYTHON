from dataclasses import dataclass
from datetime import datetime

from lib.model import Model


@dataclass
class User(Model):
    id: int
    name: str
    password: str
    created_at: datetime

    def __hash__(self):
        return hash((self.id, self.name, self.password, self.created_at))

