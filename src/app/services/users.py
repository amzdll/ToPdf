from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from src.app.db.repositories.users import user_repository
from src.app.models.schemas.user import UserBaseScheme


class UserService:

    @staticmethod
    async def create_user(session: AsyncSession, user_scheme: UserBaseScheme):
        await user_repository.create_user(session, user_scheme)
        return user_scheme

    @staticmethod
    async def get_users(session: AsyncSession) -> List[UserBaseScheme]:
        users = await user_repository.get_users(session)
        return [UserBaseScheme(id=user.id) for user in users]


user_service = UserService()
