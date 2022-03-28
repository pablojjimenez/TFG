from typing import TypedDict, Optional

from config.db import DBManager


class ListParams(TypedDict, total=False):
    sort: Optional[str]
    query: Optional[str]
    page: Optional[int]
    limit: Optional[int]


class BaseDAO:

    def __init__(self, table: str, db_url: str):
        self._db = DBManager(db_url)
        self._cur = self._db.connection.cursor()
        self._table = table

    def get_all(self, params: ListParams = None):
        if params is None:
            params = {}

        sql = "SELECT * FROM %s"

        sort = params.get('sort', '')
        query = params.get('query', '')
        limit = params.get('limit', '')
        page = params.get('page', '')

        if query != '':
            sql += f' WHERE {query} '

        if sort != '':
            asc_desc = ' DESC ' if sort[0] == '-' else ' ASC '
            sort1 = ' ORDER BY %s' + asc_desc
            if sort[0] == '-':
                sort1 = sort1 % sort[1:]
            else:
                sort1 = sort1 % sort
            sql += sort1

        if limit != '':
            sql += f' limit {limit} '
            if page != '':
                if page == 1:
                    sql += ' OFFSET 0'
                elif page == 2:
                    sql += f' OFFSET {limit}'
                else:
                    sql += f' OFFSET {(page - 1) * limit} '
        sql = sql % self._table

        out = self._cur.execute(sql)
        return out.fetchall()

    def get_one_by_id(self, id):
        out = self._cur.execute(
            "SELECT * FROM '%s' WHERE id = '%s'"
            % (self._table, id)
        )
        return out.fetchall()
