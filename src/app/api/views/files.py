import sqlalchemy.exc
from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.app.api.dependencies.database import get_async_session
from src.app.core.config import get_app_settings
from src.app.db.repositories.files import FileRepository
from src.app.models.schemas.file import FileCreate
from src.app.services.files import FileService
from src.utils.converter import PdfConverter

router = APIRouter()

settings = get_app_settings()
converter = PdfConverter(settings.imgs_storage_path)


@router.post(
    path="/upload/",
    response_model=FileCreate,
    status_code=status.HTTP_201_CREATED

)
async def upload_file(
        user_id: str,
        file: UploadFile,
        session: AsyncSession = Depends(get_async_session)
):
    return await FileService.upload_file(session, user_id, file)


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
