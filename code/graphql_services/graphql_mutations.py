import strawberry

from graphql_services.grapql_types import MyReturnType, DiseasesFilter, DiseaseDTO
from managers.utils import transform_params, remove_nulls_from_json, change_key_operators
from repositories.creator import DeceaseRepoCreator, DiseaseRepoCreator


@strawberry.type
class Mutation:

    @staticmethod
    def commpute_mutations_params(query, sort: str,
                                  page: int, limit: int):
        if query is not None:
            query = remove_nulls_from_json(query)
            query = change_key_operators(query)
            query = None if query == {} else query
        return transform_params(query, sort, page, limit)


    @strawberry.mutation
    def get_diseases(self, query: DiseasesFilter = None, sort: str = None,
                     page: int = None, limit: int = None) -> MyReturnType[DiseaseDTO]:
        cie_obj = None
        if query is not None:
            cie_obj = query.to_cie()
            query = query.dict_repr().copy()
            del query['cie_id']
            del query['cie_name']
        params = Mutation.commpute_mutations_params(query, sort, page, limit)
        diseases = DiseaseRepoCreator().factory_method()
        data = diseases.get_all(params, cie_obj)
        return MyReturnType[DiseaseDTO](data[0], data[1])
