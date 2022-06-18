import abc
from abc import abstractmethod

from config.general_config import get_config
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_repository import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository


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
        return CcaaRepository(get_config().ccaa_repo_path)


class CieRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return CieRepository(get_config().cie_repo_path)


class AgesGroupsRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return GedadRepository(get_config().gedad_repo_path)


class DiseaseRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return DiseaseRepository(
            get_config().disease_repo_path,
            CieRepoCreator().factory_method()
        )


class RazielRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return RazielRepository(
            get_config().raziel_repo_path,
            DiseaseRepoCreator().factory_method(),
            CcaaRepoCreator().factory_method(),
            AgesGroupsRepoCreator().factory_method()
        )
