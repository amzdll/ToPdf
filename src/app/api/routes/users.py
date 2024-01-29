from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.api.dependencies.database import get_async_session
from src.app.db.repositories.users import UserRepository
from src.app.models.domains.user import User

router = APIRouter()


@router.get("/")
async def get_users(
        user_repository: UserRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    users = await user_repository.get_all_users(session)
    return {"users": users}


@router.post("/add_user/{id}")
async def add_user(
        id: str,
        user_repository: UserRepository = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    new_user = User(id=int(id))
    await user_repository.create_user(session, new_user)

    return {"message": "User added successfully"}
