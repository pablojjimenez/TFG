import abc
import pandas as pd
from typing import Optional

from typing_extensions import TypedDict

from models.exceptions import IncorrectColumnNamesException, IncorrectQueryException, \
    DataIsNotAvailable


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
            raise DataIsNotAvailable(name)

    def _check_query(self, query):
        keys = query.keys()
        keys = list(map(lambda x: x.upper(), keys))
        allow = self.dataframe.columns.tolist()
        for i in keys:
            if i.upper() not in allow:
                raise IncorrectColumnNamesException(f'Incorrect query, column {i} does not exist')

        for _, value in query.items():
            for key, _ in value.items():
                if key not in ['<', '>', '==', '!=', 'like']:
                    raise IncorrectQueryException("bad formed argument: allow = ['<', '>', '==', "
                                                  "'!=', 'like']")

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
            query = self.generate_query(params['query'])
            out = self.dataframe.query(query, engine='python')
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
    def generate_query(query):
        """
        Generate str query to pandas
        :param query: json  with the constraints
        :return: the query in str
        """
        out = ''
        for k, v in list(query.items()):
            e = list(v.items())
            for element in e:
                if element[0] == 'like':
                    out += f'{k.upper()}.str.contains("{element[1]}", na=False) & '
                elif element[1] == '' and element[0] == '==':
                    out += f'{k.upper()}.isnull() & '
                elif element[1] == '' and element[0] == '!=':
                    out += f'{k.upper()}.notnull() & '
                else:
                    if isinstance(element[1], list):
                        for _e in element[1]:
                            if type(_e) == str:
                                _e = f"'{_e}'"
                            out += f'{k.upper()}{element[0]}{_e} | '
                    else:
                        out += f'{k.upper()}{element[0]}{element[1]} & '
        return out[:-3] if out != '' else 'tuple()'

    @abc.abstractmethod
    def get_one(self, id):
        """
        Get one item from the collection of objects
        :param key: Key of the collection
        :param id: key item
        :return: The object
        """
        list = self.dataframe[self.dataframe['ID'] == id].values.tolist()
        return None if len(list) == 0 else list[0]
