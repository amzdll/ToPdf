import io
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from converter.pdfconverter import PdfConverter

app = FastAPI()
converter = PdfConverter()


class ResultFile:
    filename: str
    data: io.BytesIO


app.result_file = ResultFile()


@app.post("/upload/")
async def upload(file: UploadFile):
    app.result_file.filename = file.filename
    app.result_file.data = converter.convert(file.file)
    return ["ok"]


@app.get("/download/")
async def download():
    app.result_file.data.seek(0)
    return StreamingResponse(app.result_file.data,
                             media_type="application/pdf",
                             headers={
                                 "Content-Disposition":
                                     'attachment;'
                                     'filename="' + app.result_file.filename.split(".")[0] + '.pdf"',
                                 "Content-Type": "application/pdf",
                             })


if __name__ == "__main__":
    uvicorn.run("simple_api:app", reload=True)
