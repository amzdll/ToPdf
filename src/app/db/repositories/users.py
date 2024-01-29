from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.app.models.domains.user import User


class UserRepository:
    async def create_user(self, session: AsyncSession, user: User) -> None:
        async with session.begin():
            session.add(user)

    async def get_user_by_id(self, session: AsyncSession, user_id: int):
        statement = select(User).where(User.id == user_id)
        result = await session.execute(statement)
        return result.scalar()


user_repo = UserRepository()
