from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.models.domains.user import UserModel
from src.app.models.schemas.user import UserBaseScheme


class UserRepository:
    @staticmethod
    async def create_user(session: AsyncSession, user: UserBaseScheme) -> None:
        async with session.begin():
            session.add(UserModel(**user.model_dump()))

    @staticmethod
    async def get_users(session: AsyncSession):
        statement = select(UserModel)
        result = await session.execute(statement)
        return result.scalars().all()

    @staticmethod
    async def get_user_by_id(session: AsyncSession, user_id: int):
        statement = select(UserModel).where(UserModel.id == user_id)
        result = await session.execute(statement)
        return result.scalar()


user_repository = UserRepository()
