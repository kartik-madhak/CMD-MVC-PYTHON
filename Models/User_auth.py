from dataclasses import dataclass
from datetime import datetime

from lib.model import Model


@dataclass
class User_auth(Model):
    id: int
    user_id: int
    token: str
    created_at: datetime
