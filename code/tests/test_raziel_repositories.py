import unittest

from models.raziel_model import Raziel
from tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_raziel_repository import MockRazielRepository


class TestRaziel(unittest.TestCase):

    def setUp(self):
        self.raziel_repo = MockRazielRepository(
            disease_repo=MockDiseaseRepository(MockCieRepository()),
            ccaas_repo=MockCcaaRepository(),
            gedades_repo=MockGedadRepository()
        )

    def test_get_one_complete_raziel_object(self):
        obj = self.raziel_repo.get_one(1)
        self.assertIsInstance(obj, Raziel)
