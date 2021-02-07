from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Optional

Status = Literal["delivering", "waiting", "resting"]

@dataclass
class DeliveryPerson:
    delivery_person_id: str
    state: Status
    x: int
    y: int
    max_delivery_time: Optional[int]
    updated_at: datetime

