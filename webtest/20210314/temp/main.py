from datetime import datetime
from typing import List

from app.app import App
from app.repository.memory import MemoryRepository


class Query:
    time: datetime
    query_type: str
    arguments: List[str]

    def __init__(self, query_str: str):
        """
        2020-03-04 10:30 query_type arguments
        """
        time_str = query_str[:16]
        self.time = datetime.strptime(time_str, "%Y-%m-%d %H:%M")

        query_detail = query_str[17:].split()
        self.query_type = query_detail[0]
        self.arguments = query_detail[1:]


def setup() -> App:
    repo = MemoryRepository()
    return App(repo)

def main(lines):
    app = setup()
    m = int(lines[0])  # number of setups
    for l in lines[1:m+1]:
        app.setup(l)

    for l in lines[m+1:]:
        query = Query(l)
        app.execute_query(query.time, query.query_type, *query.arguments)

if __name__ == '__main__':
    lines = [
        "1",
        "setup1",
        "2021-03-12 00:00 query_type argument1 argument2",
    ]
    main(lines)
