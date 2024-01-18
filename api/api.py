import uvicorn

from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse

from converter.converter import Converter

app = FastAPI()


@app.post("/uploadfiles/")
async def create_upload_files(
    input_files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
    pdf_files: Annotated[
        list[UploadFile], File(description="Hui")
    ]
):
    converter = Converter()
    converted_file = converter.convert(input_files[0].filename, input_files[0].file)
    pdf_files.insert(UploadFile(converted_file))

    return {"filenames": [file.filename for file in input_files]}


@app.get("/")
async def main():
    content = """
<body>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)

if __name__ == "__main__":
    uvicorn.run("api:app", reload=True)
