from app.domain.delivery_person import DeliveryPerson
from app.repository.memory import MemoryRepository
from app.domain.query import Query

class SetAvailableApplication:

    def __init__(self, repository: MemoryRepository):
        self.repo = repository

    def do(self, query: Query):
        time = query.time
        arguments = query.arguments

        delivery_person_id: str = arguments[0]
        x: int = int(arguments[1])
        y: int = int(arguments[2])
        delivery_person = DeliveryPerson(delivery_person_id, "waiting", x, y, None, time)
        self.repo.upsert_delivery_person(delivery_person)
