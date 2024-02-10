import os
from typing import BinaryIO, List

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.config import get_app_settings
from src.app.db.repositories.files import file_repository
from src.app.models.schemas.file import FileBaseScheme
from src.app.services.exceptions.incorrect_filetype import IncorrectFiletype
from src.utils.converter import PdfConverter

settings = get_app_settings()
imgs_storage_path: str = settings.imgs_storage_path


class FileService:
    __converter: PdfConverter

    def __init__(self):
        try:
            self.__converter = PdfConverter(imgs_storage_path)
        except ValueError:
            raise IncorrectFiletype()

    @staticmethod
    async def extract_filename(file: str) -> str:
        return file.split(".")[0]

    async def convert_file(
            self,
            user_id: str,
            filename: str,
            source_data: BinaryIO
    ) -> None:
        if not os.path.exists(imgs_storage_path):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="We're having trouble... Please wait"
            )

        self.__converter.convert(
            source_data=source_data,
            result_name=f"user_id_{user_id}_{filename}"
        )

    @staticmethod
    async def upload_file(
            session: AsyncSession,
            file_scheme: FileBaseScheme,
            file_data: BinaryIO
    ) -> FileBaseScheme:
        file_scheme.filename = await files_service.extract_filename(
            str(file_scheme.filename)
        )

        # local saving of a pdf file
        await files_service.convert_file(
            str(file_scheme.user_id), file_scheme.filename, file_data
        )

        # adding pdf file information to db
        await file_repository.create_file(session, file_scheme)
        return file_scheme

    @staticmethod
    async def get_files_by_user_id(
            user_id: str,
            session: AsyncSession
    ) -> List[FileBaseScheme]:
        files = await file_repository.get_files_by_user_id(
            session=session, user_id=int(user_id)
        )
        return [FileBaseScheme(**file.model_dump()) for file in files]


files_service = FileService()
