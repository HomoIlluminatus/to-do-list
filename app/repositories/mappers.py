from entities.user import User
from entities.category import Category
from models.user import UserModel
from models.category import CategoryModel


def user_to_user_model(user: User) -> UserModel:
    return UserModel(
        name=user.name,
        email=user.emial,
        hashed_password=user.hashed_password,
        role=user.role,
    )


def user_model_to_user(user: UserModel) -> User:
    return User(
        id=user.id,
        name=user.name,
        email=user.email,
        hashed_password=user.hashed_password,
        role=user.role,
    )
