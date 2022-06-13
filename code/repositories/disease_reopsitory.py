from typing import Tuple, List

from models.disease_model import Disease
from repositories.abstract_repository import AbstractRepository, ListParams


class DiseaseRepository(AbstractRepository):
    def __init__(self, name, cie_repo):
        super().__init__(name)
        self.cie_repo = cie_repo

    def get_all(self, params: ListParams = None) -> Tuple[List[Disease], int, int]:
        data, ori_tam = super().get_all(params)
        data_objs = list(map(lambda x: Disease(x[0], x[1], self.cie_repo.get_one(x[2])), data))
        return data_objs, len(data), ori_tam

    def get_one(self, id: int) -> object:
        data = super().get_one('ID', id)
        return Disease(data[0], data[1], self.cie_repo.get_one(data[2])) if data != [] else None
