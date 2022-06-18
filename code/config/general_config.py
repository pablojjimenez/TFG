from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = ''
    port: int = 0
    debug_app: str = ''
    chart_path_base: str = 'opt/'

    class Config:
        env_file = '.env'


@lru_cache()
def get_config():
    return Settings()
