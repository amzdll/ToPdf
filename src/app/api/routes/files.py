import datetime
from datetime import datetime

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import StreamingResponse

from src.app.api.dependencies.database import get_async_session
from src.app.db.repositories.files import FileRepository
from src.app.models.domains.file import File
from src.utils.converter import PdfConverter

router = APIRouter()

# todo: replace global path to relative
converter = PdfConverter(
    "/Users/glenpoin/W/Projects/Python/ToPdf/src/app/db/temp_imgs_storage/"
)


@router.post("/upload/")
async def upload(
        id: str,
        file: UploadFile,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session),
):
    filename: str = file.filename.split(".")[0]
    try:
        new_file = File(file_name=str(f"{filename}.pdf"), user_id=int(id), conversion_date=datetime.now())
        await file_repository.create_file(session, new_file)
        converter.convert(
            source_data=file.file,
            result_name=f"{id + "_" + str(filename)}"
        )
        return ["ok"]
    except ValueError:
        return ["This is all not ok..."]


@router.get("/list/")
async def list_files(
        id: str,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
) -> list[str]:
    return [file.file_name for file in await file_repository.get_all_files(session, int(id))]


@router.get("/download/")
async def download(
        id: str,
        file_repository: FileRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    a = await file_repository.get_all_files(session, int(id))
    for i in a:
        print(i.file_name)
    return ""
    return StreamingResponse(
        result_file.data, media_type="application/pdf", headers=headers
    )
