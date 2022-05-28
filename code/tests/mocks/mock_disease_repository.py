from repositories.abstract_repository import ListParams
from repositories.disease_reopsitory import DiseaseRepository


class MockDiseaseRepository(DiseaseRepository):
    def __init__(self, mock_cie_repo):
        super().__init__('tests/mocks/data/diseases', mock_cie_repo)

    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
