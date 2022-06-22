from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_creator import DiseaseRepoCreator, CieRepoCreator, \
    DeceaseRepoCreator, AgesGroupsRepoCreator
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_decease_repository import MockDeceaseRepository


class TestMockRepoCreator:
    def test_instances(self):
        obj = DiseaseRepoCreator().factory_method()
        assert isinstance(obj, MockDiseaseRepository)
        obj = CieRepoCreator().factory_method()
        assert isinstance(obj, MockCieRepository)
        obj = DeceaseRepoCreator().factory_method()
        assert isinstance(obj, MockDeceaseRepository)
        obj = AgesGroupsRepoCreator().factory_method()
        assert isinstance(obj, MockGedadRepository)

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
