import unittest

from models.disease_model import Disease
from models.raziel_model import Raziel
from models.small_models import Cie, Ccaa, Gedad
from tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_raziel_repository import MockRazielRepository


class TestRazielRepo(unittest.TestCase):

    def setUp(self):
        self.raziel_repo = MockRazielRepository(
            disease_repo=MockDiseaseRepository(MockCieRepository()),
            ccaas_repo=MockCcaaRepository(),
            gedades_repo=MockGedadRepository()
        )

    def test_get_one_complete_raziel_object(self):
        obj = self.raziel_repo.get_one(1)
        self.assertIsInstance(obj, Raziel)
        self.assertIsInstance(obj.causa.cie, Cie)
        self.assertIsInstance(obj.ccaa, Ccaa)
        self.assertIsInstance(obj.causa, Disease)
        self.assertIsInstance(obj.gedad, Gedad)

    def test_list_with_param_page1(self):
        list_param = {
            'page': 1,
            'limit': 5
        }
        obj, tam = self.raziel_repo.get_all(list_param)
        self.assertEqual(tam, 5)
        self.assertEqual(len(obj), 5)
        self.assertEqual(obj[0].id, 1)

    def test_list_with_param_page2(self):
        list_param = {
            'page': 2,
            'limit': 5
        }
        obj, tam = self.raziel_repo.get_all(list_param)
        self.assertEqual(tam, len(obj))
        self.assertEqual(tam, 5)
        self.assertEqual(obj[0].id, 6)

    def test_list_with_param_sort(self):
        list_param = {
            'sort': '-defu',
            'page': 1,
            'limit': 5
        }
        obj, tam = self.raziel_repo.get_all(list_param)
        self.assertEqual(tam, len(obj))
        self.assertEqual(tam, 5)
        self.assertEqual(obj[0].id, 11)
        self.assertEqual(obj[0].ano, 1980)

    def test_list_with_param_sort2(self):
        list_param = {
            'sort': 'defu',
            'page': 1,
            'limit': 5
        }
        obj, tam = self.raziel_repo.get_all(list_param)
        self.assertEqual(tam, len(obj))
        self.assertEqual(tam, 5)
        self.assertEqual(obj[0].id, 16)

    def test_list_with_query(self):
        list_param = {
            'query': {'ano': ('==', 1980), 'CAUSA': ('==', 1)}
        }
        obj, tam = self.raziel_repo.get_all(list_param)
        self.assertEqual(tam, 6)
        for o in obj:
            self.assertEqual(o.ano, 1980)

    def test_list_with_all_list_params(self):
        list_param = {
            'query': {'defu': ('>', 5)},
            'sort': 'cruda',
            'limit': 3,
            'page': 2
        }
        obj, tam = self.raziel_repo.get_all(list_param)
        self.assertEqual(tam, list_param['limit'])
        self.assertEqual(obj[0].id, 1)
        self.assertEqual(obj[1].id, 9)
        self.assertEqual(obj[2].id, 16)
