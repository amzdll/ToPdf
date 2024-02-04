from starlette.requests import Request
from starlette.responses import JSONResponse


async def incorrect_filetype_handler(_: Request, __: ValueError) -> JSONResponse:
    return JSONResponse(content={"detail": "Incorrect filetype"}, status_code=415)
