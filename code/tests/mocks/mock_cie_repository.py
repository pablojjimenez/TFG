from models.small_models import Cie
from repositories.abstract_repository import ListParams
from repositories.cie_repository import CieRepository


class MockCieRepository(CieRepository):
    def __init__(self):
        super().__init__(None)
        self.data = [
            ('A80', 'FIEBRE PARATIFOIDEA A'),
            ('A20', 'ENTERITIS DEBIDA A SALMONELLA')
        ]

    def get_all(self, params: ListParams = None) -> (list, int):
        objs = list(map(lambda x: Cie(id=x[0], description=x[1]), self.data))
        return objs, len(self.data)

    def get_one(self, id: int) -> object:
        objs = list(map(lambda x: Cie(id=x[0], description=x[1]), self.data))
        rtado = list(filter(lambda x: x.id == id, objs))
        return rtado[0] if len(rtado) > 0 else None
