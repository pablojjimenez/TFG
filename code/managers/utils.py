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
        'limit': limit,
        'page': page
    }
