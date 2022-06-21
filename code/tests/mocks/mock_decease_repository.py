from repositories.abstract_repository import ListParams
from repositories.decease_repository import DeceaseRepository


class MockDeceaseRepository(DeceaseRepository):
    def __init__(self, disease_repo, ccaas_repo, gedades_repo):
        super().__init__('tests/mocks/data/razielM',
                         disease_repo, ccaas_repo, gedades_repo)

    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
