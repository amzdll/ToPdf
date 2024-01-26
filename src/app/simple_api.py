import io
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from src.utils.converter import PdfConverter

app = FastAPI()
converter = PdfConverter("/home/freiqq/Projects/Python/ToPdf/src/app/db/temp_imgs_storage/")


class ResultFile:
    filename: str
    data: io.BytesIO


app.result_file = ResultFile()


class FileItem(BaseModel):
    pass


@app.post("/upload/")
async def upload(file: UploadFile):
    app.result_file.filename = file.filename
    try:
        app.result_file.data = converter.convert(
            source_data=file.file,
            result_name=f"{str(3) + "_" + file.filename}"
        )
        return ["ok"]
    except ValueError:
        return ["This is all not ok..."]


@app.get("/download/")
async def download():
    app.result_file.data.seek(0)
    headers = {
        "Content-Disposition": "attachment;"
                               'filename="' + app.result_file.filename.split(".")[0] + '.pdf"',
        "Content-Type": "application/pdf",
    }
    return StreamingResponse(
        app.result_file.data, media_type="application/pdf", headers=headers
    )


if __name__ == "__main__":
    uvicorn.run("simple_api:app", reload=True)
