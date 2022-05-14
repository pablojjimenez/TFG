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
    query = json.loads(query) if query is not None else None
    return {
        'query': query,
        'sort': sort,
        'limit': limit,
        'page': page
    }
