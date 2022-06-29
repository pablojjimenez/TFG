import abc
from abc import abstractmethod

from config.general_config import get_config
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_repository import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.decease_repository import DeceaseRepository


class RepoCreator(abc.ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def get_all_operation(self, params) -> (list, int):
        product = self.factory_method()
        return product.get_all(params)


class CcaaRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        path = get_config().ccaa_repo_path if get_config().environment != 'T' \
            else get_config().mock_ccaa_repo_path
        return CcaaRepository(path)


class CieRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        path = get_config().cie_repo_path if get_config().environment != 'T' \
            else get_config().mock_cie_repo_path
        return CieRepository(path)


class AgesGroupsRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        path = get_config().gedad_repo_path if get_config().environment != 'T' \
            else get_config().mock_gedad_repo_path
        return GedadRepository(path)


class DiseaseRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        path = get_config().disease_repo_path if get_config().environment != 'T' \
            else get_config().mock_disease_repo_path
        return DiseaseRepository(
            path,
            CieRepoCreator().factory_method()
        )


class DeceaseRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        path = get_config().raziel_repo_path if get_config().environment != 'T' \
            else get_config().mock_raziel_repo_path
        return DeceaseRepository(
            path,
            DiseaseRepoCreator().factory_method(),
            CcaaRepoCreator().factory_method(),
            AgesGroupsRepoCreator().factory_method()
        )
