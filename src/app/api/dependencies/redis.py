from functools import lru_cache

import aioredis
from fastapi import Depends
from src.app.core.config import get_app_settings

settings = get_app_settings()


@lru_cache
async def get_redis():
    redis = await aioredis.from_url(settings.redis_url)
    return redis


async def get_cached_settings(redis: aioredis.Redis = Depends(get_redis)):
    return await redis.get("settings")
