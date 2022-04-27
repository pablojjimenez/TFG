import unittest

import pandas

from models.exceptions import NoCorrectColumnsException
from services.graphic_manager import GraphicManager
from tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_raziel_repository import MockRazielRepository


class TestGraphicManager(unittest.TestCase):

    def setUp(self):
        raziel_repo = MockRazielRepository(
            disease_repo=MockDiseaseRepository(MockCieRepository()),
            ccaas_repo=MockCcaaRepository(),
            gedades_repo=MockGedadRepository()
        )
        self.manager = GraphicManager(raziel_repo)

    def test_prepare_dataframe(self):
        obj = self.manager._prepare_dataframe(None, 'GEDAD', 'DEFU')
        self.assertIsInstance(obj, pandas.Series)

    def test_invalid_vars(self):
        with self.assertRaises(NoCorrectColumnsException):
            self.manager._prepare_dataframe(None, 'AAAA', 'B')
