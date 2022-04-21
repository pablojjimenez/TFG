from repositories.abstract_repository import ListParams
from repositories.cie_repository import CieRepository


class MockCieRepository(CieRepository):
    def __init__(self):
        super().__init__('tests/mocks/data/cie')

    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
