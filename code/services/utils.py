import os


def assure_exists_directory(directory: str):
    """
    Create directory if not exists
    :param directory: directory name
    """
    isExist = os.path.exists(directory)
    if not isExist:
        os.makedirs(directory, exist_ok=False)
