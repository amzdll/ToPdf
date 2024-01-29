import io

from fastapi import APIRouter, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import StreamingResponse

from src.app.api.dependencies.database import get_async_session
from src.app.db.repositories.users import UserRepository
from src.app.models.domains.user import User
from src.utils.converter import PdfConverter

router = APIRouter()

converter = PdfConverter(
    "/home/freiqq/Projects/Python/ToPdf/src/app/db/temp_imgs_storage/"
)


class ResultFile:
    filename: str
    data: io.BytesIO


result_file = ResultFile()


@router.get("/")
async def print_id(id: str):
    return {"message": "Hello World", "id": id}


@router.post("/test_name/")
async def test_name(
    id: str,
    user_repository: UserRepository = Depends(),
    session: AsyncSession = Depends(get_async_session)
):
    new_user = User(id=int(id))
    await user_repository.create_user(session, new_user)

    return {"message": "User added successfully"}



@router.post("/upload/")
async def upload(file: UploadFile):
    result_file.filename = file.filename.split(".")[0]
    try:
        result_file.data = converter.convert(
            source_data=file.file,
            result_name=f"{id + "_" + str(result_file.filename)}"
        )
        return ["ok"]
    except ValueError:
        return ["This is all not ok..."]


@router.get("/download/")
async def download():
    result_file.data.seek(0)
    headers = {
        "Content-Disposition": "attachment;"
                               'filename="' + result_file.filename.split(".")[0] + '.pdf"',
        "Content-Type": "application/pdf",
    }
    return StreamingResponse(
        result_file.data, media_type="application/pdf", headers=headers
    )
