from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.models.domains.file import FileModel
from src.app.models.schemas.file import FileBaseScheme


class FileRepository:

    @staticmethod
    async def create_file(
            session: AsyncSession, file: FileBaseScheme) -> None:
        async with session.begin():
            session.add(FileModel(**file.model_dump()))

    @staticmethod
    async def get_all_files(
            session: AsyncSession, user_id: int
    ) -> Sequence[FileModel]:
        statement = select(FileModel).filter(FileModel.user_id == user_id)
        result = await session.execute(statement)
        return result.scalars().all()


file_repository = FileRepository()
