from models.disease_model import Disease
from repositories.abstract_repository import ListParams
from repositories.disease_reopsitory import DiseaseRepository


class MockDiseaseRepository(DiseaseRepository):
    def __init__(self, cie_repo):
        super().__init__(None, cie_repo)
        self.data = [
            (1, 'Difteria', None),
            (2, 'Poliomielitis aguda', 'A80'),
            (3, 'SIDA y VIH+', 'B20')
        ]

    def get_all(self, params: ListParams = None) -> (list, int):
        objs = list(map(lambda x: Disease(x[0], x[1], self.cie_repo.get_one(x[2]), self.data)))
        return objs, len(self.data)

    def get_one(self, id: int) -> object:
        objs = list(map(lambda x: Disease(x[0], x[1], self.cie_repo.get_one(x[2])), self.data))
        rtado = list(filter(lambda x: x.id == id, objs))
        return rtado[0] if len(rtado) > 0 else None
