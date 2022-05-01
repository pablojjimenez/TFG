import unittest

from services.predictor_manager import PredictorManager
from tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_raziel_repository import MockRazielRepository


class TestPredictor(unittest.TestCase):

    def setUp(self):
        self.raziel_repo = MockRazielRepository(
            disease_repo=MockDiseaseRepository(MockCieRepository()),
            ccaas_repo=MockCcaaRepository(),
            gedades_repo=MockGedadRepository()
        )
        self.predict = PredictorManager(self.raziel_repo)

    def test_deaths_prediction(self):
        self.predict.deaths_forecasting({
            'query': {'GEDAD': ('==', 99),'causa': ('==', 999), 'CCAA': ('==', 99)}
        }, 'ANO', 'DEFU')
