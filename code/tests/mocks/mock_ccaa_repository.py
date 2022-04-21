from models.small_models import Ccaa
from repositories.abstract_repository import ListParams
from repositories.ccaa_repository import CcaaRepository


class MockCcaaRepository(CcaaRepository):
    def __init__(self):
        super().__init__('tests/mocks/data/ccaas')
        
    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
