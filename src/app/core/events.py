# from src.app.api.dependencies.redis import get_redis_connection
# from src.app.core.config import get_app_settings


async def startup_event():
    pass
    # redis_conn = get_redis_connection()
    # settings_json = get_app_settings().model_dump_json()
    # redis_conn.set("settings", settings_json)


async def shutdown_event() -> None:
    pass
