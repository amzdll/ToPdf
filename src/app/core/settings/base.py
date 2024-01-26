from enum import Enum

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev
    database_url: PostgresDsn

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
