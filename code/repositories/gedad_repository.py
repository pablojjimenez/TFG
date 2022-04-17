from models.small_models import Gedad
from repositories.abstract_repository import AbstractRepository, ListParams


class GedadRepository(AbstractRepository):
    def __init__(self, manager):
        super().__init__(manager)

    def get_all(self, params: ListParams = None) -> list:
        out = super().get_all(params)
        return list(map(lambda x: Gedad(id=x[1], description=x[2]), out))

    def get_one(self, id) -> list:
        out = super().get_one(id)
        return Gedad(id=out[0][1], description=out[0][2])
