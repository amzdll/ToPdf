from pydantic import PostgresDsn

from src.app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    database_url: PostgresDsn
