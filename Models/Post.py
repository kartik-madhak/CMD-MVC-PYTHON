from dataclasses import dataclass
from datetime import datetime

from lib.model import Model


@dataclass
class Post(Model):
    id: int
    name: str
    content: str
    created_at: datetime
