from src.app.db.queries import queries
from src.app.db.repositories.base import BaseRepository
from models.domain.user import User


class UserRepository(BaseRepository):
    async def create_user(
            self,
            *,
            id: int
    ) -> User:
        user = User(id=id)

        async with self.connection.transaction():
            user_row = await queries.create_new_user(
                self.connection,
                id=user.id
            )

        return user.copy(update=dict(user_row))
