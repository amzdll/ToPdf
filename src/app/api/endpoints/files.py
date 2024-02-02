import sqlalchemy.exc
from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.app.api.dependencies.database import get_async_session
from src.app.core.config import get_app_settings
from src.app.db.repositories.files import FileRepository
from src.app.models.schemas.file import FileCreate
from src.app.services.files import files_service, FileService
from src.utils.converter import PdfConverter

router = APIRouter()

settings = get_app_settings()
converter = PdfConverter(settings.imgs_storage_path)


@router.post(
    path="/upload_file/",
    response_model=FileCreate,
    status_code=status.HTTP_201_CREATED

)
async def upload_file(
        user_id: str,
        file: UploadFile,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        return await FileService.upload_file(session, user_id, file)
    except sqlalchemy.exc.IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Who is it?!")
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This is all not ok...")
    except FileNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="We're having trouble... Please wait")


@router.get("/get_filenames/")
async def get_filenames(
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
