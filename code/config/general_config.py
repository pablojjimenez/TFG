from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int
    debug_app: str
    chart_base_app: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_config():
    return Settings()
