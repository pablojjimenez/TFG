import strawberry

from graphql_services.grapql_types import MyReturnType, DiseasesFilter, \
    DiseaseDTO, DiseasesSearchFilter, DeceaseDTO, DeceaseFilter
from managers.utils import transform_params, remove_nulls_from_json, \
    change_key_operators
from repositories.creator import DiseaseRepoCreator, CieRepoCreator, DeceaseRepoCreator


@strawberry.type
class Mutation:

    @staticmethod
    def commpute_mutations_params(query, sort: str,
                                  page: int, limit: int):
        if query is not None:
            query = remove_nulls_from_json(query.dict_repr())
            query = change_key_operators(query)
            query = None if query == {} else query
        return transform_params(query, sort, page, limit)

    @strawberry.mutation
    def get_diseases(self, query: DiseasesFilter = None, sort: str = None,
                     page: int = None, limit: int = None) -> MyReturnType[DiseaseDTO]:
        params = Mutation.commpute_mutations_params(query, sort, page, limit)
        diseases = DiseaseRepoCreator().get_all_operation(params)
        return MyReturnType[DiseaseDTO](diseases[0], diseases[1])

    @strawberry.mutation
    def look_for_diseases(self, query: DiseasesSearchFilter = None, sort: str = None,
                          page: int = None, limit: int = None) -> MyReturnType[DiseaseDTO]:
        diseases_repo = DiseaseRepoCreator().factory_method()
        if query.cieName is not None:
            cie_repo = CieRepoCreator().factory_method()
            cies = cie_repo.get_all(transform_params({'description': {'like': query.cieName}}))
            disease_query = None
            if query.diseaseName is not None:
                disease_query = {'name': {'like': query.diseaseName}}
            diseases = diseases_repo.get_all(
                transform_params(disease_query, sort, page, limit), cies
            )
        else:
            diseases = diseases_repo.get_all(
                transform_params({'name': {'like': query.diseaseName}}, sort, page, limit)
            )

        return MyReturnType[DiseaseDTO](diseases[0], diseases[1])

    @strawberry.mutation
    def get_deceases(self, query: DeceaseFilter = None, sort: str = None,
                     page: int = None, limit: int = None) -> MyReturnType[DeceaseDTO]:
        params = Mutation.commpute_mutations_params(query, sort, page, limit)
        deceases = DeceaseRepoCreator().get_all_operation(params)
        return MyReturnType[DeceaseDTO](deceases[0], deceases[1])

    @strawberry.mutation
    def search_deceases(self, query: DiseasesSearchFilter = None, sort: str = None,
                        page: int = None, limit: int = None) -> MyReturnType[DeceaseDTO]:
        deceases = DeceaseRepoCreator().factory_method()
        cies = []

        if query.cieName is not None:
            cie_repo = CieRepoCreator().factory_method()
            cies = cie_repo.get_all(transform_params({'description': {'like': query.cieName}}))[0]

        if query.diseaseName is not None:
            disease_query = {'name': {'like': query.diseaseName}}
        else:
            cies_ids = list(map(lambda c: c.id, cies))
            disease_query = {'cie': {'==': cies_ids}}

        diseases_repo = DiseaseRepoCreator().factory_method()
        diseases = diseases_repo.get_all(
            transform_params(disease_query, sort, page, limit), cies
        )[0]
        diseases_ids = list(map(lambda d: d.id, diseases))
        rtado = deceases.get_all(
            transform_params({'causa': {'==': diseases_ids}}, sort, page, limit)
        )
        return MyReturnType[DeceaseDTO](rtado[0], rtado[1])
