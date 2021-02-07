from dataclasses import dataclass
from typing import List

from .closed_time import ClosedTime

@dataclass
class Restaurant:
    restaurant_id: str
    x: int
    y: int
    closed_times: List[ClosedTime]
    deposit: int = 0
