from models.small_models import Gedad
from repositories.abstract_repository import ListParams
from repositories.gedad_repository import GedadRepository


class MockGedadRepository(GedadRepository):
    def __init__(self):
        super().__init__(None)
        self.data = [
            (1, '15 a 24 años'),
            (2, '25 a 34 años'),
            (3, '35 a 44 años')
        ]

    def get_all(self, params: ListParams = None) -> (list, int):
        objs = map(lambda x: Gedad(id=x[0], description=x[1]), self.data)
        return objs, len(self.data)

    def get_one(self, id: int) -> object:
        objs = list(map(lambda x: Gedad(id=x[0], description=x[1]), self.data))
        rtado = list(filter(lambda x: x.id == id, objs))
        return rtado[0] if len(rtado) > 0 else None
