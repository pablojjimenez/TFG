import unittest

from models.disease_model import Disease
from models.small_models import Cie

from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository


class TestDiseaseRepo(unittest.TestCase):

    def setUp(self):
        self.raziel_repo = MockDiseaseRepository(MockCieRepository())

    def test_get_one_uncomplete_disease_object(self):
        obj = self.raziel_repo.get_one(2)
        self.assertIsInstance(obj, Disease)
        self.assertEqual(obj.cie, None)

    def test_get_one_complete_disease_object(self):
        obj = self.raziel_repo.get_one(1)
        self.assertIsInstance(obj, Disease)
        self.assertIsInstance(obj.cie, Cie)
