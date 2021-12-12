from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    BACKEND_CORS_ORIGINS: List[str] = ['*']
    PROJECT_NAME: str
    STATIC_DIR: str = 'static'


settings = Settings()
