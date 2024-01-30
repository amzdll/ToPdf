from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from src.app.models.domains.file import File


class FileRepository:
    async def create_file(self, session: AsyncSession, file: File) -> None:
        async with session.begin():
            session.add(file)

    async def get_all_files(self, session: AsyncSession, id: int) -> List[File]:
        statement = select(File).filter(File.user_id == id)
        result = await session.execute(statement)
        return result.scalars().all()


file_repository = FileRepository()
