import aioredis
from aioredis import Redis


async def get_redis(settings):
    redis = aioredis.from_url(settings.redis_url, decode_responses=True)
    return redis
