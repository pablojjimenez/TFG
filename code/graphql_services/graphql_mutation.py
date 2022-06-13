import strawberry

from graphql_services.graph_types import MyReturnType, CCAAFilter, CcaaDTO, DiseasesFilter, DiseaseDTO, RazielFilter, \
    RazielDTO
from managers.utils import remove_nulls_from_json, change_key_operators, transform_params
from repositories.ccaa_repository import CcaaRepository
from repositories.cie_repository import CieRepository
from repositories.disease_reopsitory import DiseaseRepository
from repositories.gedad_repository import GedadRepository
from repositories.raziel_repository import RazielRepository


@strawberry.type
class Mutation:
    @staticmethod
    def commpute_mutations_params(query, sort: str,
                                  page: int, limit: int):
        print(query)
        if query is not None:
            query = remove_nulls_from_json(query.dict_repr())
            query = change_key_operators(query)
        return transform_params(query, sort, page, limit)

    @strawberry.mutation
    def get_ccaas(self, query: CCAAFilter = None, sort: str = None,
                  page: int = None, limit: int = None) -> MyReturnType[CcaaDTO]:
        params = Mutation.commpute_mutations_params(query, sort, page, limit)
        ccaas = CcaaRepository('data/ccaas').get_all(params)
        return MyReturnType[CcaaDTO](ccaas[0], ccaas[1])

    @strawberry.mutation
    def get_diseases(self, query: DiseasesFilter = None, sort: str = None,
                     page: int = None, limit: int = None) -> MyReturnType[DiseaseDTO]:
        params = Mutation.commpute_mutations_params(query, sort, page, limit)
        diseases = DiseaseRepository('data/diseases', CieRepository('data/cie')).get_all(params)
        return MyReturnType[DiseaseDTO](diseases[0], diseases[1])

    @strawberry.mutation
    def get_raziel(self, query: RazielFilter = None, sort: str = None,
                   page: int = None, limit: int = None) -> MyReturnType[RazielDTO]:
        params = Mutation.commpute_mutations_params(query, sort, page, limit)
        raziel = RazielRepository(
            'data/raziel',
            DiseaseRepository('data/diseases', CieRepository('data/cie')),
            CcaaRepository('data/ccaas'),
            GedadRepository('data/grupos_edad')
        ).get_all(params)
        return MyReturnType[RazielDTO](raziel[0], raziel[1])
