from abc import ABCMeta, abstractmethod
from datetime import datetime


class RepositoryAbs(metaclass=ABCMeta):

    @abstractmethod
    def set_time(self, time: datetime):
        pass

    @abstractmethod
    def get_time(self) -> datetime:
        pass
