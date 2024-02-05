from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.app.api.dependencies.database import get_async_session
from src.app.models.schemas.user import UserBaseScheme
from src.app.services.users import user_service

router = APIRouter()


@router.get(
    "/",
    response_model=List[UserBaseScheme],
    status_code=status.HTTP_200_OK
)
async def get_users(
        session: AsyncSession = Depends(get_async_session)
) -> List[UserBaseScheme]:
    users = await user_service.get_users(session)
    return users


@router.post(
    "/add_user/{id}",
    response_model=UserBaseScheme,
    status_code=status.HTTP_201_CREATED
)
async def add_user(
        user_scheme: UserBaseScheme,
        session: AsyncSession = Depends(get_async_session)
) -> UserBaseScheme:
    return await user_service.create_user(session, user_scheme)
