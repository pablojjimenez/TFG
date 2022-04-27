import abc
import pandas as pd
from typing import Optional, TypedDict


class ListParams(TypedDict, total=False):
    sort: Optional[str]
    query: Optional[TypedDict]
    page: Optional[int]
    limit: Optional[int]
    group: Optional[str]


class AbstractRepository(abc.ABC):

    def __init__(self, name):
        try:
            self.dataframe = pd.read_csv(f"{name}.csv")
        except FileNotFoundError:
            self.dataframe = pd.DataFrame()

    @abc.abstractmethod
    def get_all(self, params: ListParams = None) -> list:
        """
        Get all objects from the database.
        :param params: ListParams
        :return: list of objects and total number of objects
        """
        out = self._filter_dataframe(params)
        return out.values.tolist()

    def _filter_dataframe(self, params):
        out = self.dataframe
        keys = params.keys()
        if 'query' in keys:
            self._check_query(params['query'])
            query = ' & '.join([f'{k.upper()}{v[0]}{v[1]}' for k, v in params['query'].items()])
            out = self.dataframe.query(query)
        if 'sort' in keys:
            asc = params['sort'][0] == '-'
            sort_by = params['sort'][1:] if asc else params['sort']
            out = out.sort_values(by=sort_by.upper(), ascending=asc)
        if 'limit' in keys:
            page = params['page'] if not params['page'] or params['page'] != 1 else 0
            ini = page * params['limit'] - params['limit'] if page != 0 else 0
            end = params['limit'] * page if page != 0 else params['limit']
            out = out.iloc[ini:end]
        return out

    @abc.abstractmethod
    def get_one(self, key: str, id) -> object:
        list = self.dataframe[self.dataframe[key] == id].values.tolist()
        return None if len(list) == 0 else list[0]
