from pydantic import EmailStr
from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .common import Common
from entities.user import UserRole


class UserModel(Common):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(255), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole), nullable=False, server_default=UserRole.USER.name
    )
