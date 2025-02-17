from abc import ABC, abstractmethod

import bcrypt
from fastapi import Depends
from pydantic import EmailStr

from core.errors.user import UserNotFoundError
from entities.user import User, UserRole
from repositories.user import AbstractUserRepository, UserRepository


class AbstractUserService(ABC):
    def __init__(self, rep: AbstractUserRepository):
        self._rep = rep

    @abstractmethod
    async def get_user_by_id_or_raise(self, user_id: int) -> User: ...

    @abstractmethod
    async def get_user_by_email_or_raise(self, email: EmailStr) -> User: ...

    @abstractmethod
    async def get_users_list(self) -> list[User]: ...

    @abstractmethod
    async def create_user(
        self,
        name: str,
        email: EmailStr,
        password: str,
        role: UserRole = UserRole.USER,
    ) -> User: ...

    @abstractmethod
    async def delete_user(self, user_id: int) -> None: ...


class UserService(AbstractUserService):
    def __init__(
        self, rep: AbstractUserRepository = Depends(UserRepository)
    ) -> None:
        super().__init__(rep)

    async def get_user_by_id_or_raise(self, user_id: int) -> User:
        user = await self._rep.get_by_id(user_id)
        if user is None:
            raise UserNotFoundError(user_id)
        return user

    async def get_user_by_email_or_raise(self, email: EmailStr) -> User:
        user = await self._rep.get_by_email(email)
        if user is None:
            raise UserNotFoundError(email)
        return user

    async def get_users_list(self) -> list[User]:
        return await self._rep.get_list()

    async def create_user(
        self,
        name: str,
        email: EmailStr,
        password: str,
        role: UserRole = UserRole.USER,
    ) -> User:
        try:
            self._validate(name, email, password)
        except:
            ...

        hashed_password = self._hash_password(password)
        user = User(
            id=0,
            name=name,
            email=email,
            hashed_password=hashed_password,
            role=role,
        )
        return await self._rep.add(user)

    async def delete_user(self, user_id: int) -> None:
        await self._rep.delete(user_id)

    @staticmethod
    def _hash_password(password: str) -> str:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def _validate(name: str, email: EmailStr, password: str) -> None: ...
