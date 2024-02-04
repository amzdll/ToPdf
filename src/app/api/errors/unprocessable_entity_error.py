from sqlalchemy.exc import IntegrityError
from starlette.requests import Request
from starlette.responses import JSONResponse


async def unprocessable_entity_error_handler(
        _: Request, __: IntegrityError
) -> JSONResponse:
    return JSONResponse({"detail": "Unprocessable entity"}, status_code=422)
