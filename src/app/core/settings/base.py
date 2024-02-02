from enum import Enum

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class AppEnvTypes(Enum):
    dev: str = "dev"


class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev

    imgs_storage_path: str

    db_user: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str

    @property
    def database_url_asyncpg(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"

    class Config:
        env_file = ".env"
