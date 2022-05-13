from models.small_models import Gedad
from repositories.abstract_repository import AbstractRepository, ListParams


class GedadRepository(AbstractRepository):
    def __init__(self, name):
        super().__init__(name)

    def get_all(self, params: ListParams = None) -> list:
        data = super().get_all(params)
        data_objs = list(map(lambda x: Gedad(id=x[0], description=x[1]), data))
        return data_objs, len(data_objs)

    def get_one(self, id) -> list:
        data = super().get_one('ID', id)
        return Gedad(id=data[0], description=data[1]) if data else None
