from enum import Enum

from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev
