import abc
import pandas as pd
from typing import Optional

from typing_extensions import TypedDict

from models.exceptions import NoCorrectColumnsException, IncorrectQueryException, DataIsNotAvaible


class ListParams(TypedDict, total=False):
    sort: Optional[str]
    query: Optional[TypedDict]
    page: Optional[int]
    limit: Optional[int]


class AbstractRepository(abc.ABC):

    def __init__(self, name):
        try:
            self.dataframe = pd.read_csv(f"{name}.csv")
        except FileNotFoundError:
            raise DataIsNotAvaible(name)

    def _check_query(self, query):
        keys = query.keys()
        keys = list(map(lambda x: x.upper(), keys))
        allow = self.dataframe.columns.tolist()
        for i in keys:
            if i.upper() not in allow:
                raise NoCorrectColumnsException(f'no colum {i}')

        for _, value in query.items():
            for key, _ in value.items():
                if key not in ['<', '>', '==', '!=']:
                    raise IncorrectQueryException("bad formed argument: allow = ['<', '>', '==']")

    @abc.abstractmethod
    def get_all(self, params: ListParams = None) -> list:
        """
        Get all objects from the database.
        :param params: ListParams
        :return: list of objects and total number of objects
        """
        out = self.filter_dataframe(params)
        return out.values.tolist()

    def filter_dataframe(self, params):
        """
        Filter dataframe
        :param params: ListParams
        :return: dataframe filtered
        """
        out = self.dataframe
        params = params if params is not None else {}
        if params.get('query') is not None:
            self._check_query(params['query'])
            query = self.generate_vector_query(params['query'])
            out = self.dataframe.query(query)
        if params.get('limit') is not None:
            page = 0 if params['page'] is None or params['page'] == 1 else params['page']
            ini = page * params['limit'] - params['limit'] if page != 0 else 0
            end = params['limit'] * page if page != 0 else params['limit']
            out = out.iloc[ini:end]
        if params.get('sort') is not None:
            asc = params['sort'][0] == '-'
            sort_by = params['sort'][1:] if asc else params['sort']
            out = out.sort_values(by=sort_by.upper(), ascending=asc)
        return out

    @staticmethod
    def generate_vector_query(query):
        """
        Generate str query to pandas
        :param query: json  with the constraints
        :return: the query in str
        """
        out = []
        for k, v in list(query.items()):
            e = list(v.items())
            for element in e:
                if element[1] == '' and element[0] == '==':
                    out.append(f'{k.upper()}.isnull()')
                elif element[1] == '' and element[0] == '!=':
                    out.append(f'{k.upper()}.notnull()')
                else:
                    out.append(f'{k.upper()}{element[0]}{element[1]}')
        return ' & '.join(out)

    @abc.abstractmethod
    def get_one(self, key: str, id) -> object:
        """
        Get one item from the collection of objects
        :param key: Key of the collection
        :param id: key item
        :return: The object
        """
        list = self.dataframe[self.dataframe[key] == id].values.tolist()
        return None if len(list) == 0 else list[0]
