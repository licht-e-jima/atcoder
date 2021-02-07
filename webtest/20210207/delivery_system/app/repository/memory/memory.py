from datetime import datetime
from typing import Dict, List

from app.domain.restaurant import Restaurant
from app.domain.delivery_person import DeliveryPerson
from app.domain.order import Order
from app.domain.query import Query

class MemoryRepository:
    restaurants: Dict[str, Restaurant]
    delivery_people: Dict[str, DeliveryPerson]
    orders_restaurants: Dict[str, Order]
    delivery_people_orders: Dict[str, Order]
    orders: List[Order]
    queries: List[Query]

    def __init__(self):
        self.restaurants = {}
        self.delivery_people = {}
        self.orders_restaurants = {}
        self.delivery_people_orders = {}
        self.orders = []
        self.queries = []

    def add_query(self, query: Query):
        self.queries.append(query)

    def pop_queries(self, time: datetime):
        filtered = list(filter(lambda q: q.time <= time, self.queries))
        self.query = list(filter(lambda q: time < q.time, self.queries))
        return filtered

    def create_restaurant(self, restaurant: Restaurant):
        assert isinstance(restaurant, Restaurant)
        self.restaurants[restaurant.restaurant_id] = restaurant

    def upsert_delivery_person(self, delivery_person: DeliveryPerson):
        assert isinstance(delivery_person, DeliveryPerson)
        if delivery_person.delivery_person_id in self.delivery_people:
            old_delivery_person = self.delivery_people[delivery_person.delivery_person_id]
            old_delivery_person.x = delivery_person.x
            old_delivery_person.y = delivery_person.y
            old_delivery_person.max_delivery_time = delivery_person.max_delivery_time
            old_delivery_person.updated_at = delivery_person.updated_at
        else:
            self.delivery_people[delivery_person.delivery_person_id] = (delivery_person)

    def get_available_delivery_people(self):
        people = self.delivery_people.values()
        people = list(filter(
            lambda p: p.state == 'waiting',
            people
        ))
        return people

    def create_order(self, order: Order):
        assert  isinstance(order, Order)
        self.orders.append(order)
        self.orders_restaurants[order.restaurant_id] = order
        # この時点では誰が配達するかは決まってないので delivery_people_orders は更新しない

    def order_denied_cz_closed(self, order: Order):
        assert order in self.orders
        order.status = "CLOSED TIME"

    def order_denied_cz_no_delivery_person(self, order: Order):
        assert order in self.orders
        order.status = "NO DELIVERY PERSON"
