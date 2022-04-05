from repositories.abstract_repository import AbstractRepository, ListParams


class VarsRepository(AbstractRepository):
    def __init__(self, dao_manager):
        super().__init__(dao_manager)

    def get_all(self, params: ListParams = None) -> (list, int):
        return super().get_all(params)

    def get_one(self, id: int) -> object:
        return super().get_one(id)
