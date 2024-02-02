from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.models.domains.file import FileModel


class FileRepository:

    @staticmethod
    async def create_file(session: AsyncSession, file: FileModel) -> None:
        async with session.begin():
            session.add(file)

    @staticmethod
    async def get_all_files(
            session: AsyncSession, user_id: int
    ) -> Sequence[FileModel]:
        statement = select(FileModel).filter(FileModel.user_id == user_id)
        result = await session.execute(statement)
        return result.scalars().all()


file_repository = FileRepository()
