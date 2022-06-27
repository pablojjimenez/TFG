from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = ''
    port: int = 0
    debug_app: str = ''
    chart_path_base: str = '/tmp'
    environment: str = 'T'
    ccaa_repo_path: str = ''
    cie_repo_path: str = ''
    gedad_repo_path: str = ''
    disease_repo_path: str = ''
    raziel_repo_path: str = ''
    mock_ccaa_repo_path: str = 'tests/data/ccaas'
    mock_cie_repo_path: str = 'tests/data/cie'
    mock_gedad_repo_path: str = 'tests/data/grupos_edad'
    mock_disease_repo_path: str = 'tests/data/diseases'
    mock_raziel_repo_path: str = 'tests/data/razielM'

    class Config:
        env_file = '.env'


@lru_cache()
def get_config():
    return Settings()
