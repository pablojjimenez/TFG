import abc
from abc import abstractmethod

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
        return CcaaRepository('data/ccaas')


class CieRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return CieRepository('data/cie')


class AgesGroupsRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return GedadRepository('data/grupos_edad')


class DiseaseRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return DiseaseRepository('data/diseases', CieRepoCreator().factory_method())


class DeceaseRepoCreator(RepoCreator):
    """
    Concrete CCAA repository creator
    """

    def factory_method(self):
        return DeceaseRepository(
            'data/raziel',
            DiseaseRepoCreator().factory_method(),
            CcaaRepoCreator().factory_method(),
            AgesGroupsRepoCreator().factory_method()
        )
