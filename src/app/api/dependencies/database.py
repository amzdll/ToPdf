from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncSession
)

from src.app.core.config import get_app_settings

settings = get_app_settings()

engine = create_async_engine(
    url=settings.database_url_asyncpg,
    # echo=True
)

session_maker = async_sessionmaker(engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_maker() as session:
        yield session
