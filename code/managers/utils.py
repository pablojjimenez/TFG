from typing import Dict

from repositories.abstract_repository import AbstractRepository


def transform_params(query: Dict[str, Dict[str, str]],
                     sort: str = None, page: int = None, limit: int = None):
    return {
        'query': query,
        'sort': sort,
        'limit': limit,
        'page': page
    }


def call_repository_get_all(repo: AbstractRepository, query: Dict[str, Dict[str, str]], sort: str,
                            page: int, limit: int):
    """
    Aux function used by all endpoints to generate queries
    :param repo: concerned repository
    :param query: query dict
    :param sort: sort param
    :param page: number page param
    :param limit: recovery limit number
    :return: {items, length} return format
    """
    p = transform_params(query, sort, page, limit)
    objs, tam = repo.get_all(p)
    return {
        'items': objs,
        'length': tam
    }

def remove_nulls_from_json(data: dict):
    dd = {}
    for k, v in data.items():
        if isinstance(v, dict):
            r = remove_nulls_from_json(v)
            if len(r) != 0:
                dd[k] = r
        elif v is not None or k == 'neq':
            dd[k] = v
    return dd




def change_key_operators(data: dict):
    """

    :param data:
    :return:
    """
    changes = {
        'eq': '==',
        'gt': '>',
        'lt': '<',
        'neq': '!='
    }
    items = list(data.items())
    for k, v in items:
        if isinstance(v, dict):
            change_key_operators(v)
        else:
            if k in list(map(lambda x: x[0] if x[0] != 'like' else [], items)):
                data[changes[k]] = data[k]
                del data[k]
    return data
