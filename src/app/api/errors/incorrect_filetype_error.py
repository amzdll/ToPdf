from typing import Type

from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import status

from src.app.services.exceptions.incorrect_filetype import IncorrectFiletype


async def incorrect_filetype_handler(
        _: Type[Request], __: Type[IncorrectFiletype]) -> JSONResponse:
    return JSONResponse(
        content={"detail": "Incorrect filetype"},
        status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
    )
