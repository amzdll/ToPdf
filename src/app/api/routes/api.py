from fastapi import APIRouter

from src.app.api.routes import file

router = APIRouter()

router.include_router(file.router, prefix="/{id}", tags=["files"])
