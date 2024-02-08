from pydantic_settings import BaseSettings


class RedisSettings(BaseSettings):
    redis_host: str
    redis_port: int
    redis_name: str

    class Config:
        env_file = ".redis.env"


def get_redis_settings() -> RedisSettings:
    return RedisSettings()
