import pytest

from repositories.creator import DeceaseRepoCreator, DiseaseRepoCreator, CcaaRepoCreator


@pytest.fixture
def mock_decease_repo():
    return DeceaseRepoCreator().factory_method()


@pytest.fixture
def mock_disease():
    return DiseaseRepoCreator().factory_method()


@pytest.fixture
def mock_ccaas():
    return CcaaRepoCreator().factory_method()
