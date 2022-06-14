import os
from typing import Dict
import arrow

from config.general_config import CHARTS_BASE_PATH


def ensure_directory_exists(directory: str):
    """
    Create directory if not exists
    :param directory: directory name
    """
    is_exist = os.path.exists(directory)
    if not is_exist:
        os.makedirs(directory, exist_ok=False)
    remove_pasts_images()


def remove_pasts_images():
    deleteTime = arrow.now().shift(minutes=-5)
    for f in os.listdir(CHARTS_BASE_PATH):
        f = os.path.join(CHARTS_BASE_PATH, f)
        itemTime = arrow.get(os.stat(f).st_mtime)
        if itemTime < deleteTime:
            if os.path.isfile(f):
                os.remove(f)


def transform_params(query: Dict[str, Dict[str, str]],
                     sort: str = None, page: int = None, limit: int = None):
    return {
        'query': query,
        'sort': sort,
        'limit': limit,
        'page': page
    }
