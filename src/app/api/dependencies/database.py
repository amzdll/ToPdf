# from typing import AsyncGenerator, Callable, Type
#
# from asyncpg.connection import Connection
# from asyncpg.pool import Pool
# from fastapi import Depends
# from starlette.requests import Request
#
# from src.app.db.repositories.base import BaseRepository
#
#
# def _get_db_pool(request: Request) -> Pool:
#     return request.app.state.pool
#
#
# async def _get_connection_from_pool(
#     pool: Pool = Depends(_get_db_pool),
# ) -> AsyncGenerator[Connection, None]:
#     async with pool.acquire() as conn:
#         yield conn
#
#
# def get_repository(repo_type: Type[BaseRepository],) -> Callable[[Connection], BaseRepository]:
#     def _get_repo(conn: Connection = Depends(_get_connection_from_pool),) -> BaseRepository:
#         return repo_type(conn)
#     return _get_repo
from sqlalchemy import create_engine

from src.app.core.config import get_app_settings

settings = get_app_settings()
# print(settings.database_url)
# engine = create_engine(
#     url=settings.database_url,
#     echo=True,
#     pool_size=5,
#     max_overflow=10
# )

# with engine.connect() as connection:
#     print(connection.execute("SELECT VERSION()"))

