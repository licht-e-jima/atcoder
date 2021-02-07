フォルダごとアップロードできると思っていましたが、コードを写しきることができませんでした。
解ききれなかったのは、DDD で実装を初めてしまったためです。

私の計画力と実装力の実力の至らないところでした。
しかし、せっかく実装しましたので、下にコードを記述しておきます。

```
├── app
│   ├── __pycache__
│   │   └── app.cpython-39.pyc
│   ├── app.py
│   ├── application
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── order_application.cpython-39.pyc
│   │   │   ├── set_avaliable_application.cpython-39.pyc
│   │   │   └── setup_application.cpython-39.pyc
│   │   ├── order_application.py
│   │   ├── set_avaliable_application.py
│   │   └── setup_application.py
│   ├── domain
│   │   ├── delivery_person
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   └── delivery_person.cpython-39.pyc
│   │   │   └── delivery_person.py
│   │   ├── order
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   └── order.cpython-39.pyc
│   │   │   └── order.py
│   │   ├── query
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   └── query.cpython-39.pyc
│   │   │   └── query.py
│   │   ├── restaurant
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   ├── closed_time.cpython-39.pyc
│   │   │   │   └── restaurant.cpython-39.pyc
│   │   │   ├── closed_time.py
│   │   │   └── restaurant.py
│   │   └── service
│   │       └── restaurant
│   │           ├── __init__.py
│   │           └── restaurant_factory.py
│   └── repository
│       ├── __pycache__
│       │   └── memory.cpython-39.pyc
│       └── memory
│           ├── __init__.py
│           ├── __pycache__
│           │   ├── __init__.cpython-39.pyc
│           │   └── memory.cpython-39.pyc
│           └── memory.py
├── explanation.md
└── main.py
```

というフォルダ構成になっています。

`app/application/__init__.py`

```python
from .order_application import OrderApplication
from .set_avaliable_application import SetAvailableApplication
from .setup_application import SetupApplication
```

`app/application/order_application/py`

```python
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
```

`app/application/set_avaiilable_application.py`

```python
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
```

`app/application/setup_application.py`

```python
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
```

`app/domain/delivery_person/__init__.py`

```python
from .delivery_person import DeliveryPerson
```

`app/domain/delivery_person/delivery_person.py`

```python
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
```

`app/domain/order/__init__.py`

```python
from .order import Order
```

`app/domain/order/order.py`

```python
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
```

`app/domain/query/__init__.py`

```python
from .query import Query
```

`app/domain/query/query.py`

```python
from datetime import datetime
from dataclasses import dataclass
from typing import List

@dataclass
class Query:
    time: datetime
    query_type: str
    arguments: List[str]
```

`app/restaurant/__init__.py`

```python
from .restaurant import Restaurant
from .closed_time import ClosedTime
```

`app/restaurant/closed_time.py`

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ClosedTime:
    """標準ライブラリの datetime.time が 24:00 に対応していないため、独自に実装する
    """
    start_h: int
    start_m: int
    end_h: int
    end_m: int

    def __post_init__(self):
        assert (
            0 <= self.start_h <= 23 and
            0 <= self.end_h <= 24 and
            0 <= self.start_m <= 60 and
            0 <= self.end_m <= 60 and
            (
                self.start_h < self.end_h or
                (
                    self.start_h == self.end_h and
                    self.start_m < self.end_m
                )
            )
        ), f"START: {self.start_h}:{self.start_m}\tEND: {self.end_h}:{self.end_m}"

    @classmethod
    def from_str(cls, time_span_str: str) -> "ClosedTime":
        start_time, end_time = time_span_str.split("-")
        start_h = int(start_time[:2])
        start_m = int(start_time[3:])
        end_h = int(end_time[:2])
        end_m = int(end_time[3:])
        return cls(start_h, start_m, end_h, end_m)

    def is_within_closing_time(self, t: datetime) -> bool:
        if self.start_h == self.end_h:
            return (
                self.start_h == t.hour and
                self.start_m <= t.minute < self.end_m
            )
        else:
            return (
                (
                    self.start_h == t.hour and
                    self.start_m <= t.minute
                ) or
                self.start_h < t.hour < self.end_h or
                (
                    t.hour == self.end_h and
                    t.minute < self.end_m
                )
            )
```

`app/restaurant/restaurant.py`

```python
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
```

`app/repository/memory/__init__.py`

```python
from .memory import MemoryRepository
```

`app/repository/memory/memory.py`

```python
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
```

`app/app.py`

```python
from datetime import datetime
from typing import Tuple, List

from .application import SetupApplication, SetAvailableApplication, OrderApplication
from .domain.query import Query


class App:
    def __init__(
        self,
        repository
    ):
        self.setup = SetupApplication(repository)
        self.order = OrderApplication(repository)
        self.set_avaliable = SetAvailableApplication(repository)
        self.repo = repository

    def query(self, query: str):
        main_q = self.parse_query(query)
        # 未実行のクエリを実行する
        queries = self.repo.pop_queries(main_q.time)
        queries.append(main_q)
        queries.sort(key=lambda q: q.time)

        for q in queries:
            self.execute(q)

    def do_all_remain_query(self):
        queries = self.repo.queries
        for q in queries:
            self.execute(q)

    def execute(self, query: Query):
        if query.query_type == "order":
            self.order.do(query)
        elif query.query_type == "set_available":
            self.set_avaliable.do(query)


    def create_restaurant(self, query: str):
        self.setup.do(query)

    def parse_query(self, query: str) -> Query:
        time_str = query[:16]
        time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        detail = query[17:]
        parsed_query = detail.split()
        query_type = parsed_query[0]
        arguments = parsed_query[1:]
        return Query(time, query_type, arguments)
```

`main.py`

```python
import sys

from app.app import App
from app.repository.memory.memory import MemoryRepository


def main(lines):
    app = setup()
    m = int(lines[0])  # number of restaulants
    for r in lines[1:m+1]:
        app.create_restaurant(r)

    for o in lines[m+1:]:
        app.query(o)

    app.do_all_remain_query()

def setup() -> App:
    repo = MemoryRepository()
    return App(repo)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
```
