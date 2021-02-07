from dataclasses import dataclass
from typing import Literal, Optional


Status = Literal["ordered", "CLOSED TIME", "NO DELIVERY PERSON", "accepted"]

@dataclass
class Order:
    restaurant_id: str
    price: int
    to_x: int
    to_y: int
    status: Status
    delivery_person_id: Optional[str] = None
    delivery_fee: int = 0
