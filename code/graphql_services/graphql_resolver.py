import strawberry

from graphql_services.grapql_types import MyReturnType, DiseaseDTO, GedadDTO, CcaaDTO, CieDTO
from managers.utils import transform_params
from repositories.creator import DiseaseRepoCreator, AgesGroupsRepoCreator, \
    CieRepoCreator, CcaaRepoCreator


class GraphQLResolver:
    """
    Class for abstracting information retrieval from different repositories
    """
    params = transform_params(None, None, None, None)

    @staticmethod
    def get_ccaas():
        rtado = CcaaRepoCreator().get_all_operation(GraphQLResolver.params)
        return MyReturnType[CcaaDTO](rtado[0], rtado[1])

    @staticmethod
    def get_cies():
        rtado = CieRepoCreator().get_all_operation(GraphQLResolver.params)
        return MyReturnType[CieDTO](rtado[0], rtado[1])

    @staticmethod
    def get_diseases():
        rtado = DiseaseRepoCreator().get_all_operation(GraphQLResolver.params)
        return MyReturnType[DiseaseDTO](rtado[0], rtado[1])

    @staticmethod
    def get_ages_groups():
        rtado = AgesGroupsRepoCreator().get_all_operation(GraphQLResolver.params)
        return MyReturnType[GedadDTO](rtado[0], rtado[1])


@strawberry.type
class Query:
    ccaas: MyReturnType[CcaaDTO] = strawberry.field(resolver=GraphQLResolver.get_ccaas)
    cies: MyReturnType[CieDTO] = strawberry.field(resolver=GraphQLResolver.get_cies)
    diseases: MyReturnType[DiseaseDTO] = strawberry.field(resolver=GraphQLResolver.get_diseases)
    ages_groups: MyReturnType[GedadDTO] = strawberry.field(resolver=GraphQLResolver.get_ages_groups)
