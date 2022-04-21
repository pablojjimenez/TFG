from models.small_models import Gedad
from repositories.abstract_repository import ListParams
from repositories.gedad_repository import GedadRepository


class MockGedadRepository(GedadRepository):
    def __init__(self):
        super().__init__('tests/mocks/data/grupos_edad')
        
    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
