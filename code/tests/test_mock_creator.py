from repositories.cie_repository import CieRepository
from repositories.creator import DiseaseRepoCreator, CieRepoCreator, DeceaseRepoCreator, AgesGroupsRepoCreator
from repositories.decease_repository import DeceaseRepository
from repositories.disease_repository import DiseaseRepository
from repositories.gedad_repository import GedadRepository


class TestMockRepoCreator:
    def test_instances(self):
        obj = DiseaseRepoCreator().factory_method()
        assert isinstance(obj, DiseaseRepository)
        obj = CieRepoCreator().factory_method()
        assert isinstance(obj, CieRepository)
        obj = DeceaseRepoCreator().factory_method()
        assert isinstance(obj, DeceaseRepository)
        obj = AgesGroupsRepoCreator().factory_method()
        assert isinstance(obj, GedadRepository)

    def test_creator_operation(self):
        obj = DiseaseRepoCreator().get_all_operation({})
        assert obj[1] == 3
        obj = CieRepoCreator().get_all_operation({})
        assert obj[1] == 4
        obj = DeceaseRepoCreator().get_all_operation({})
        assert obj[1] == 16
        obj = AgesGroupsRepoCreator().get_all_operation({})
        assert obj[1] == 4

    def test_decease_basic_query(self):
        list_param = {
            'query': {'defu': {'>': 5}},
            'sort': 'cruda',
            'limit': 3,
            'page': 2
        }
        obj, tam = DeceaseRepoCreator().get_all_operation(list_param)
        assert tam == list_param['limit']
        assert obj[0].id == 15
        assert obj[1].id == 14
        assert obj[2].id == 9

    def test_create_decease_repository(self):
        deceases_repo = DeceaseRepoCreator().factory_method()
        assert isinstance(deceases_repo, DeceaseRepository)

    def test_create_disease_repository(self):
        disease_repo = DiseaseRepoCreator().factory_method()
        assert isinstance(disease_repo, DiseaseRepository)
