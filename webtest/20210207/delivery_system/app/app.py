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

