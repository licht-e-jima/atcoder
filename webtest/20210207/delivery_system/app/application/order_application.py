from datetime import datetime
from typing import List

from app.domain.order import Order
from app.domain.restaurant import Restaurant
from app.repository.memory import MemoryRepository
from app.domain.query import Query

class OrderApplication:

    def __init__(self, repository: MemoryRepository):
        self.repo = repository

    def do(self, query: Query):
        time = query.time
        arguments: List[str] = query.arguments
        restaurant_id: str = arguments[0]
        price: int = int(arguments[1])
        to_x: int = int(arguments[2])
        to_y: int = int(arguments[3])
        order = Order(restaurant_id, price, to_x, to_y, "ordered")

        self.repo.create_order(order)
        restaurant = self.repo.restaurants[order.restaurant_id]

        status = self.assign_order(time, restaurant, order)
        if status == "CLOSED TIME":
            self.repo.order_denied_cz_closed(order)
        elif status == "NO DELIVERY PERSON":
            self.repo.order_denied_cz_no_delivery_person(order)
        else:
            pass

    def calc_delivery_fee(self, from_x: int, from_y: int, to_x: int, to_y):
        distance = abs(from_x - to_x) + abs(from_y - to_y)

    def assign_order(self, time: datetime, restaurant: Restaurant, order: Order):
        if any(map(lambda c: c.is_within_closing_time(time), restaurant.closed_times)):
            return "CLOSED TIME"

        people = self.repo.get_available_delivery_people()
        if not people:
            return "NO DELIVERY PERSON"
