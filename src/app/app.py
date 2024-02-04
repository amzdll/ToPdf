from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError

from fastapi.middleware.cors import CORSMiddleware

from src.app.api.errors.http_error import http_error_handler
from src.app.api.errors.incorrect_filetype_error import incorrect_filetype_handler
from src.app.api.errors.unprocessable_entity_error import unprocessable_entity_error_handler

from src.app.api.views.api import router as api_router


def get_application() -> FastAPI:
    application = FastAPI()

    application.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(ValueError, incorrect_filetype_handler)
    application.add_exception_handler(IntegrityError, unprocessable_entity_error_handler)

    application.include_router(api_router, prefix="")
    return application


app = get_application()
