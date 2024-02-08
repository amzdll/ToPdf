import json
from types import SimpleNamespace
from typing import Dict, Type

from src.app.api.dependencies.redis import get_redis_connection
from src.app.core.settings.app import AppSettings
from src.app.core.settings.base import AppEnvTypes, BaseAppSettings
from src.app.core.settings.development import DevAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings
}

r = get_redis_connection()


def format_settings(config) -> json:
    settings: Dict = config.__dict__
    settings.update({
        "database_url": config.database_url,
        "database_url_asyncpg": config.database_url_asyncpg
    })
    settings.pop("app_env")
    return json.dumps(settings, indent=4)


def cache_settings():
    app_env = BaseAppSettings().app_env  # type: ignore[call-arg]
    config = environments[app_env]()
    if r.get("settings") is None:
        json_settings = format_settings(config)
        r.set("settings", json_settings)


def get_cached_settings() -> SimpleNamespace | None:
    if r.get("settings") is not None:
        settings = json.loads(r.get("settings"))
        return SimpleNamespace(**settings)
    return None


def get_app_settings() -> SimpleNamespace:
    cached_settings = get_cached_settings()
    if cached_settings is None:
        cache_settings()
    return cached_settings if cached_settings is not None \
        else get_cached_settings()
