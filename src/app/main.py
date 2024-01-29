import uvicorn
from fastapi import FastAPI

from src.app.api.routes.api import router as api_router
from src.app.core.config import get_app_settings
from src.app.core.events import (
    create_start_app_handler,
    create_stop_app_handler
)


def get_application() -> FastAPI:

    application = FastAPI()
    application.include_router(api_router, prefix="")

    settings = get_app_settings()

    application.add_event_handler(
        "startup",
        create_start_app_handler(application, settings),
    )
    application.add_event_handler(
        "shutdown",
        create_stop_app_handler(application),
    )

    return application


app = get_application()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# uvicorn src.app.main:app --reload
