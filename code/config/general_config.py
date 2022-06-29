from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 5000
    openapi_path: str = '/docs'
    debug_app: str = 'F'
    chart_path_base: str = '/tmp'
    environment: str = 'T'
    ccaa_repo_path: str = 'data/ccaas'
    cie_repo_path: str = 'data/cie'
    gedad_repo_path: str = 'data/grupos_edad'
    disease_repo_path: str = 'data/diseases'
    raziel_repo_path: str = 'data/raziel'

    class Config:
        env_file = '.env'


@lru_cache()
def get_config():
    return Settings()
