from sqlalchemy.exc import IntegrityError
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi import status


async def unprocessable_entity_error_handler(
    _: Request, __: IntegrityError
) -> JSONResponse:
    return JSONResponse(
        {"detail": "Unprocessable entity"},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )
