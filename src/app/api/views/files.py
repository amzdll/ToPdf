from datetime import datetime
from typing import BinaryIO

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.app.api.dependencies.database import get_async_session
from src.app.core.config import get_app_settings
from src.app.db.repositories.files import FileRepository
from src.app.models.schemas.file import FileBaseScheme
from src.app.services.files import FileService
from src.utils.converter import PdfConverter

router = APIRouter()

settings = get_app_settings()
converter = PdfConverter(settings.imgs_storage_path)


@router.post(path="/upload/",
             response_model=FileBaseScheme,
             status_code=status.HTTP_201_CREATED)
async def upload_file(
        file: UploadFile,
        user_id: str,
        session: AsyncSession = Depends(get_async_session)
) -> FileBaseScheme:
    file_scheme: FileBaseScheme = FileBaseScheme(
        filename=file.filename,
        conversion_date=datetime.now(),
        user_id=int(user_id)
    )
    file_data: BinaryIO = file.file
    return await FileService.upload_file(session, file_scheme, file_data)


@router.get("/files/")
async def get_files(
        user_id: str,
        session: AsyncSession = Depends(get_async_session)
) -> list[str]:
    return await FileService.get_filenames(user_id=user_id, session=session)


@router.get("/download/")
async def download(
        id: str,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    pass
