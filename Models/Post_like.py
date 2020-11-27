from dataclasses import dataclass

from lib.model import Model


@dataclass
class Post_like(Model):
    user_id: int
    post_id: str
