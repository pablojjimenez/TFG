from repositories.abstract_repository import ListParams
from repositories.raziel_repository import RazielRepository


class MockRazielRepository(RazielRepository):
    def __init__(self, disease_repo, ccaas_repo, gedades_repo):
        super().__init__(None, disease_repo, ccaas_repo, gedades_repo)
        self.data = [
            (1, 2020, 1, 1, 1, 2, 0, 0, 0.0, 0.0, 2.9, 0.0, 0.0, 0.0, 0.0),
            (1, 2020, 2, 2, 2, 2, 0, 0, 0.0, 0.0, 2.9, 0.0, 0.0, 0.0, 0.0)
        ]

    def get_all(self, params: ListParams = None) -> (list, int):
        objs = list(map(lambda d: self._transform_to_model(d), self.data))
        return objs, len(objs)

    def get_one(self, id: int) -> object:
        objs = list(filter(lambda d: d.id == id, self.get_all()[0]))
        return objs[0] if len(objs) > 0 else None
