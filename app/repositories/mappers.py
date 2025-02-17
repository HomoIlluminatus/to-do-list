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


def category_to_category_model(category: Category) -> CategoryModel:
    return CategoryModel(
        id=category.id,
        user_id=category.user_id,
        title=category.title,
        description=category.description,
    )


def category_model_to_category(category: CategoryModel) -> Category:
    return Category(
        user_id=category.user_id,
        title=category.title,
        description=category.description,
    )
