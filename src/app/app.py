from fastapi import FastAPI

from src.app.api.routes.api import router as api_router


def get_application() -> FastAPI:

    application = FastAPI()
    application.include_router(api_router, prefix="")
    return application


app = get_application()

