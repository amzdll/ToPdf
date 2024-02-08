from datetime import datetime
from typing import BinaryIO, List

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.app.api.dependencies.database import get_async_session
from src.app.core.config import get_app_settings
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


@router.get(
    "/",
    response_model=List[FileBaseScheme],
    status_code=status.HTTP_200_OK
)
async def get_files(
        user_id: str,
        session: AsyncSession = Depends(get_async_session),
) -> List[FileBaseScheme]:

    return await FileService.get_files_by_user_id(
        user_id=user_id, session=session)


@router.get("/download/",
            status_code=status.HTTP_200_OK)
async def download(
        file_scheme: FileBaseScheme,
        session: AsyncSession = Depends(get_async_session)
):
    pass
