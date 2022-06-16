from repositories.creator import RepoCreator
from tests.mocks.mock_ccaa_repository import MockCcaaRepository
from tests.mocks.mock_cie_repository import MockCieRepository
from tests.mocks.mock_disease_repository import MockDiseaseRepository
from tests.mocks.mock_gedad_repository import MockGedadRepository
from tests.mocks.mock_raziel_repository import MockRazielRepository


class CcaaRepoCreator(RepoCreator):
    def factory_method(self):
        return MockCcaaRepository()


class CieRepoCreator(RepoCreator):
    def factory_method(self):
        return MockCieRepository()


class AgesGroupsRepoCreator(RepoCreator):
    def factory_method(self):
        return MockGedadRepository()


class DiseaseRepoCreator(RepoCreator):
    def factory_method(self):
        return MockDiseaseRepository(CieRepoCreator().factory_method())


class RazielRepoCreator(RepoCreator):
    def factory_method(self):
        return MockRazielRepository(
            DiseaseRepoCreator().factory_method(),
            CcaaRepoCreator().factory_method(),
            AgesGroupsRepoCreator().factory_method()
        )
