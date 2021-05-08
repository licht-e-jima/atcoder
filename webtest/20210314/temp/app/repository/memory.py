from collections import deque
from datetime import datetime

from .repository_abs import RepositoryAbs


class MemoryRepository(RepositoryAbs):

    def __init__(self):
        self.__time = datetime.strptime("2000-01-01 00:00", "%Y-%m-%d %H:%M")

    def set_time(self, time: datetime):
        self.__time = time

    def get_time(self) -> datetime:
        return self.__time
