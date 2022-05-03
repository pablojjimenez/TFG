import os

def assure_exists_directory(directory: str):
    """
    Create directory if not exists
    :param directory: directory name
    """
    script_dir = os.path.dirname(__file__)
    results_dir = os.path.join(script_dir, directory)

    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)
