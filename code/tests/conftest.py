import pytest

from tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_decease_repository import MockDeceaseRepository


@pytest.fixture
def mock_decease_repo():
    return MockDeceaseRepository(
        disease_repo=MockDiseaseRepository(MockCieRepository()),
        ccaas_repo=MockCcaaRepository(),
        gedades_repo=MockGedadRepository()
    )


@pytest.fixture
def mock_disease():
    return MockDiseaseRepository(MockCieRepository())
