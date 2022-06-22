import os
from typing import Dict

from repositories.abstract_repository import AbstractRepository


def ensure_directory_exists(directory: str):
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
