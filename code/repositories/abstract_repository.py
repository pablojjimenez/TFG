import abc

from dao.base_dao import ListParams


class AbstractRepository(abc.ABC):

    def __init__(self, dao_manager):
        self.dao_manager = dao_manager

    def get_all(self, params: ListParams = None) -> list:
        return self.dao_manager.get_all(params)

    def get_one(self, id: int) -> object:
        return self.dao_manager.get_one_by_id(id)[0]
