import pytest

from tests.unit_tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.unit_tests.mocks.mock_cie_repository import MockCieRepository
from tests.unit_tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.unit_tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.unit_tests.mocks.mock_raziel_repository import MockRazielRepository


@pytest.fixture
def mock_raziel_repo():
    return MockRazielRepository(
        disease_repo=MockDiseaseRepository(MockCieRepository()),
        ccaas_repo=MockCcaaRepository(),
        gedades_repo=MockGedadRepository()
    )


@pytest.fixture
def mock_disease():
    return MockDiseaseRepository(MockCieRepository())
