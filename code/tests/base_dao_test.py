from dao.base_dao import BaseDAO


class BaseDAOTest(BaseDAO):
    """
    BaseDAO Test Class
    -------------------
    It is using a fake sqlite database for tests
    """
    def __init__(self, table: str):
        super().__init__(table, 'db_test.db')
