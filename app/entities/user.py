from enum import Enum

from pydantic import BaseModel, EmailStr


class UserRole(Enum):
    USER = "user"
    ADMIN = "admin"


class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    hashed_password: str
    role: UserRole = UserRole.USER.name
