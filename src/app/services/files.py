from datetime import datetime
from typing import BinaryIO

from fastapi import UploadFile, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.config import get_app_settings
from src.app.db.repositories.files import file_repository
from src.app.models.domains.file import FileModel
from src.app.models.schemas.file import FileCreate
from src.utils.converter import PdfConverter

settings = get_app_settings()
imgs_storage_path: str = settings.imgs_storage_path


class FileService:
    __converter: PdfConverter = PdfConverter(imgs_storage_path)

    @staticmethod
    async def extract_filename(file: str) -> str:
        return file.split(".")[0]

    async def convert_file(
            self,
            user_id: str,
            filename: str,
            source_data: BinaryIO
    ):
        self.__converter.convert(
            source_data=source_data,
            result_name=f"user_id_{user_id}_{filename}"
        )

    @staticmethod
    async def upload_file(
            session: AsyncSession,
            user_id: str,
            file: UploadFile
    ) -> FileCreate:
        filename: str = await files_service.extract_filename(file.filename)
        new_file = FileModel(
            filename=str(filename),
            user_id=int(user_id),
            conversion_date=datetime.now()
        )

        try:
            await file_repository.create_file(session, new_file)
            await files_service.convert_file(user_id, filename, file.file)
            return FileCreate(
                filename=filename,
                conversion_date=datetime.now()
            )
        except FileNotFoundError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="We're having trouble... Please wait"
            )

    @staticmethod
    async def get_filenames(user_id: str, session: AsyncSession) -> [..., str]:
        files = await file_repository.get_all_files(session, int(user_id))
        return [file.filename for file in files]


files_service = FileService()
