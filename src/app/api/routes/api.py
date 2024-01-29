from fastapi import APIRouter

from src.app.api.routes import files, users

router = APIRouter()

router.include_router(files.router, prefix="/user/{id}/files", tags=["files"])
router.include_router(users.router, prefix="/user", tags=["users"])
