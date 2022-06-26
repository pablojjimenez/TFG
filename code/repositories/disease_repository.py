from typing import Tuple, List

from models.disease_model import Disease
from models.small_models import Cie
from repositories.abstract_repository import AbstractRepository, ListParams


class DiseaseRepository(AbstractRepository):
    def __init__(self, name, cie_repo):
        super().__init__(name)
        self.cie_repo = cie_repo

    def get_all(self, params: ListParams = None, cie: Cie = None) -> Tuple[List[Disease], int]:
        cies = None
        if cie is not None:
            cies = self.cie_repo.get_like(cie)

        if cie is not None and len(cies) > 0:
            cie_queries = list(map(lambda x: x.id, cies))
            params['query'] = {
                'cie': {
                    '==': cie_queries
                },
            }
        data = super().get_all(params)
        print(cies)

        data_objs = list(map(lambda x: Disease(x[0], x[1], self.cie_repo.get_one(x[2])), data))
        print(data_objs)
        return data_objs, len(data)

    def get_one(self, id: int) -> object:
        data = super().get_one(id)
        return Disease(data[0], data[1], self.cie_repo.get_one(data[2])) if data != [] else None
