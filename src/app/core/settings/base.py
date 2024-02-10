from enum import Enum

from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    dev: str = "dev"
#   other_variant: str = "other_variant"
#    ...


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev
