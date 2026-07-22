from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: Optional[int] = None
    copies: int = 1

    def to_dict(self):
        return asdict(self)
