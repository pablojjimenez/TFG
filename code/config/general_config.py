from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = ''
    port: int = 5000
    openapi_path: str = '/docs'
    debug_app: str = ''
    chart_path_base: str = '/tmp'
    ccaa_repo_path: str = ''
    cie_repo_path: str = ''
    gedad_repo_path: str = ''
    disease_repo_path: str = ''
    raziel_repo_path: str = ''

    class Config:
        env_file = '.env'


@lru_cache()
def get_config():
    return Settings()
