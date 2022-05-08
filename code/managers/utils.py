import json
import os


def assure_exists_directory(directory: str):
    """
    Create directory if not exists
    :param directory: directory name
    """
    is_exist = os.path.exists(directory)
    if not is_exist:
        os.makedirs(directory, exist_ok=False)


def transform_params(sort: str = None, query: str = None, page: int = None, limit: int = None):
    return {
        'query': json.loads(query),
        'sort': sort,
        'limit': limit,
        'page': page
    } if sort is not None and query is not None and page is not None and limit is not None else {}
