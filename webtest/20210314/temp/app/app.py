from datetime import datetime

from app.repository import RepositoryAbs


class App:

    def __init__(self, db: RepositoryAbs) -> None:
        self.db = db

    def setup(self, value: str):
        pass

    def execute_query(self, time: datetime, query: str, *args):
        self.db.set_time(time)
        if query == "query type":
            pass
        else:
            raise Exception(f"Must not reached: {query}")
