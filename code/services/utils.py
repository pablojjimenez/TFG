import os


def assure_exists_directory(directory: str):
    """
    Create directory if not exists
    :param directory: directory name
    """
    exists = os.path.exists(directory)
    if not exists:
        os.makedirs(directory, exist_ok=False)
