from typing import Dict, Type

from src.app.core.settings.app import AppSettings
from src.app.core.settings.base import AppEnvTypes, BaseAppSettings
from src.app.core.settings.development import DevAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings
}


def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()
