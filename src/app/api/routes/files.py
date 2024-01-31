from datetime import datetime

import sqlalchemy.exc
from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.api.dependencies.database import get_async_session
from src.app.core.config import get_app_settings
from src.app.db.repositories.files import FileRepository
from src.app.models.domains.file import File
from src.app.services.files import files_service
from src.utils.converter import PdfConverter

router = APIRouter()

settings = get_app_settings()
converter = PdfConverter(settings.imgs_storage_path)


@router.post("/upload/")
async def upload(
        user_id: str,
        file: UploadFile,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session),
):
    try:
        filename: str = await files_service.extract_filename(file.filename)
        new_file = (
            File(file_name=str(filename),
                 user_id=int(user_id),
                 conversion_date=datetime.now())
        )
        await file_repository.create_file(session, new_file)
        await files_service.convert_file(user_id, filename, file.file)
        return ["Ok"]
    except sqlalchemy.exc.IntegrityError:
        return ["Who is it?!"]
    except ValueError:
        return ["This is all not ok..."]
    except FileNotFoundError:
        return ["We're having trouble... Please wait"]


@router.get("/list/")
async def list_files(
        id: str,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
) -> list[str]:
    files = await file_repository.get_all_files(session, int(id))
    return [file.file_name for file in files]


@router.get("/download/")
async def download(
        id: str,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    pass
