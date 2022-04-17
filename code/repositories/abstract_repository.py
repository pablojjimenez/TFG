import abc
from typing import Optional, TypedDict


class ListParams(TypedDict, total=False):
    sort: Optional[str]
    query: Optional[str]
    page: Optional[int]
    limit: Optional[int]


class AbstractRepository(abc.ABC):

    def __init__(self, dao_manager):
        self.dao_manager = dao_manager

    @abc.abstractmethod
    def get_all(self, params: ListParams = None) -> (list, int):
        """
        Get all objects from the database.
        :param params: ListParams
        :return: (list, int) - list of objects and total number of objects
        """
        pass

    @abc.abstractmethod
    def get_one(self, id: int) -> object:
        pass
