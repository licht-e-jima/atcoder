from ..repository.memory.memory import MemoryRepository
from ..domain.restaurant import Restaurant, ClosedTime

class SetupApplication:
    def __init__(self, repository: MemoryRepository):
        self.repo = repository

    def do(self, query: str):
        info = query.split()
        restaurant_id = info[0]
        x = int(info[1])
        y = int(info[2])
        closed_times = [ClosedTime.from_str(i) for i in info[3:]]
        restaurant = Restaurant(restaurant_id, x, y, closed_times)
        self.repo.create_restaurant(restaurant)
