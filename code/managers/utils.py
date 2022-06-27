from typing import Dict


def transform_params(query: Dict[str, Dict[str, str]],
                     sort: str = None, page: int = None, limit: int = None):
    return {
        'query': query,
        'sort': sort,
        'limit': limit,
        'page': page
    }
