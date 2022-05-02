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
        df = self.predict.deaths_forecasting(None, 'ANO', 'DEFU')
        self.assertEqual(len(df.columns.tolist()), 16)
        expected_columns = ['ds', 'trend', 'yhat_lower', 'yhat_upper', 'trend_lower', 'trend_upper', 'additive_terms', 'additive_terms_lower', 'additive_terms_upper', 'yearly', 'yearly_lower', 'yearly_upper', 'multiplicative_terms', 'multiplicative_terms_lower', 'multiplicative_terms_upper', 'yhat']
        for c in df.columns.tolist():
            self.assertIn(c, expected_columns)
