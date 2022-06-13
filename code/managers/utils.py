import os
from typing import Dict


def assure_exists_directory(directory: str):
    """
    Create directory if not exists
    :param directory: directory name
    """
    is_exist = os.path.exists(directory)
    if not is_exist:
        os.makedirs(directory, exist_ok=False)


def transform_params(query: Dict[str, Dict[str, str]],
                     sort: str = None, page: int = None, limit: int = None):
    return {
        'query': query,
        'sort': sort,
        'limit': limit if limit <= 100 else 100,
        'page': page
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
            if k in list(map(lambda x: x[0], items)):
                data[changes[k]] = data[k]
                del data[k]
    return data
