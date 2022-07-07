from models.small_models import Cie
from repositories.abstract_repository import AbstractRepository, ListParams


class CieRepository(AbstractRepository):
    def __init__(self, name):
        super().__init__(name)

    def get_all(self, params: ListParams = None) -> (list, int):
        data = super().get_all(params)
        objs = list(map(lambda x: Cie(id=x[0], name=x[1]), data))
        return objs, len(data)

    def get_one(self, id: str) -> object:
        data = super().get_one(id)
        return Cie(id=data[0], name=data[1]) if data else None
