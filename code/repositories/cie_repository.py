from models.small_models import Cie
from repositories.abstract_repository import AbstractRepository, ListParams


class CieRepository(AbstractRepository):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_query_from_cie(cie):
        out = {}
        if cie.id is not None:
            out.update({'id': {'like': cie.id}})
        if cie.description is not None:
            out.update({'description': {'like': cie.description}})
        return {
            'query': out
        }

    def get_all(self, params: ListParams = None) -> (list, int):
        data = super().get_all(params)
        objs = list(map(lambda x: Cie(id=x[0], description=x[1]), data))
        return objs, len(data)

    def get_like(self, cie: Cie):
        data = super().get_all(CieRepository.get_query_from_cie(cie))
        objs = list(map(lambda x: Cie(id=x[0], description=x[1]), data))
        return objs

    def get_one(self, id: str) -> object:
        data = super().get_one(id)
        return Cie(id=data[0], description=data[1]) if data else None
