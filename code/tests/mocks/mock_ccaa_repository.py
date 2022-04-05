from models.small_models import Ccaa
from repositories.abstract_repository import ListParams
from repositories.ccaa_repository import CcaaRepository


class MockCcaaRepository(CcaaRepository):
    def __init__(self):
        super().__init__(None)
        self.data = [
            (1, 'Andalucía'),
            (2, 'Comunidad de Madrid'),
            (3, 'Extremadura')
        ]

    def get_all(self, params: ListParams = None) -> (list, int):
        return map(lambda x: Ccaa(id=x[0], name=x[1]), self.data), len(self.data)

    def get_one(self, id: int) -> object:
        objs = list(map(lambda x: Ccaa(id=x[0], name=x[1]), self.data))
        rtado = list(filter(lambda x: x.id == id, objs))
        return rtado[0] if len(rtado) > 0 else None
