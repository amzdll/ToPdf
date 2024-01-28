import io

from fastapi import APIRouter, UploadFile, Depends
from starlette.responses import StreamingResponse

from src.app.api.dependencies.database import get_repository
from src.app.db.repositories.users import UserRepository
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


@router.post("/hui/")
async def hui(
    id: str,
    users_repo: UserRepository = Depends(get_repository(UserRepository))
):
    await users_repo.create_user(id=int(id))


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
