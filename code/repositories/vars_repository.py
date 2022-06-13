from models.small_models import Vars
from repositories.abstract_repository import AbstractRepository, ListParams


class VarsRepository(AbstractRepository):
    def __init__(self, name):
        super().__init__(name)

    def get_all(self, params: ListParams = None) -> (list, int):
        obj = super().get_all(params)
        data_objs = list(map(lambda x: Vars(id=x[0], description=x[1]), obj))
        return data_objs, len(data_objs)

    def get_one(self, id: int):
        return super().get_one(id)
