from models.small_models import Sex
from repositories.abstract_repository import AbstractRepository, ListParams
from models.raziel_model import Raziel


class RazielRepository(AbstractRepository):
    def __init__(self, dao_manager, disease_repo, ccaas_repo, gedades_repo):
        super().__init__(dao_manager)
        self.ccaas_repo = ccaas_repo
        self.disease_repo = disease_repo
        self.gedades_repo = gedades_repo

    def _transform_to_model(self, tuple: tuple) -> object:
        params = {
            'id': tuple[0],
            'ano': tuple[1],
            'causa': self.disease_repo.get_one(tuple[2]),
            'sexo': Sex.MALE if tuple[3] == 1 else Sex.FEMALE,
            'ccaas': self.ccaas_repo.get_one(tuple[4]),
            'gedad': self.gedades_repo.get_one(tuple[5]),
            'defu': tuple[6],
            'avp': tuple[7],
            'cruda': tuple[8],
            'tavp': tuple[9],
            'edad': tuple[10],
            'tasae': tuple[11],
            'tavpe': tuple[12],
            'tasaw': tuple[13],
            'tasavpw': tuple[14]
        }
        return Raziel(params)

    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
