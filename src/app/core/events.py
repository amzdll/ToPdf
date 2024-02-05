import aioredis
from src.app.core.config import get_app_settings


async def startup_event():
    settings = get_app_settings()
    redis = await aioredis.from_url(settings.redis_url)
    await redis.set("settings", settings.model_dump_json())


async def shutdown_event() -> None:
    pass