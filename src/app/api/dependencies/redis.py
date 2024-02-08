import redis

from src.app.core.redis_config import get_redis_settings

redis_settings = get_redis_settings()

r = redis.Redis(
    host=redis_settings.redis_host,
    port=redis_settings.redis_port,
    decode_responses=True
)


def get_redis_connection():
    return r
