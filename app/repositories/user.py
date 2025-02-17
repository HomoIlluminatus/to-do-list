from abc import ABC, abstractmethod

from pydantic import EmailStr
import sqlalchemy as sa

from entities.user import User
from models.user import UserModel
from .base import BaseRepository
from .mappers import user_model_to_user, user_to_user_model


class AbstractUserRepository(ABC, BaseRepository[User]):
    @abstractmethod
    async def get_by_email(self, email: EmailStr) -> User | None: ...


class UserRepository(AbstractUserRepository):
    async def get_by_id(self, user_id) -> User | None:
        queryset = await self._session.execute(
            sa.select(UserModel).where(User.id == user_id)
        )
        user = queryset.scalars().first()
        return user_model_to_user(user) if user else None

    async def get_by_email(self, email: EmailStr) -> User | None:
        queryset = await self._session.execute(
            sa.select(UserModel).where(UserModel.email == email)
        )
        user = queryset.scalars().first()
        return user_model_to_user(user) if user else None

    async def get_list(self) -> list[User]:
        queryset = await self._session.execute(sa.select(UserModel))
        users = queryset.scalars().all()
        return [user_model_to_user(user) for user in users]

    async def add(self, user: User) -> User:
        self._session.add(user_to_user_model(user))
        await self._session.commit()
        return user

    async def delete(self, user_id) -> None:
        await self._session.execute(
            sa.delete(UserModel).where(UserModel.id == user_id)
        )
