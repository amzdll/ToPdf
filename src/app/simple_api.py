import io
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from src.utils.converter import PdfConverter

app = FastAPI()
converter = PdfConverter("/src/app/database/temp_imgs_storage/")


class ResultFile:
    filename: str
    data: io.BytesIO


app.result_file = ResultFile()


class FileItem(BaseModel):
    pass
