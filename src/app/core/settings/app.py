from pydantic import PostgresDsn

from src.app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    database_url: PostgresDsn

    max_connection_count: int = 10
    min_connection_count: int = 10

