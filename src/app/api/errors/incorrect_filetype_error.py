from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import status


async def incorrect_filetype_handler(
        _: Request, __: ValueError) -> JSONResponse:
    return JSONResponse(
        content={"detail": "Incorrect filetype"},
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    )
