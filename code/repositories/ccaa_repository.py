from models.small_models import Ccaa
from repositories.abstract_repository import AbstractRepository, ListParams


class CcaaRepository(AbstractRepository):
    def __init__(self, name):
        super().__init__(name)

    def get_all(self, params: ListParams = None) -> (list, int, int):
        data, ori_tam = super().get_all(params)
        data_objs = list(map(lambda x: Ccaa(id=x[0], name=x[1]), data))
        return data_objs, len(data_objs), ori_tam

    def get_one(self, id: int) -> object:
        data = super().get_one('ID', id)
        return Ccaa(id=data[0], name=data[1]) if data else None
