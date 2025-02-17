from abc import abstractmethod

import sqlalchemy as sa
from .base import BaseRepository
from .mappers import category_model_to_category, category_to_category_model
from entities.category import Category
from models.category import CategoryModel


class AbstractCategoryRepository(BaseRepository[Category]):
    @abstractmethod
    async def get_user_categories_list(
        self, user_id: int
    ) -> list[Category]: ...


class CategoryRepository(AbstractCategoryRepository):
    async def get_by_id(self, category_id) -> Category | None:
        queryset = await self._session.execute(
            sa.select(CategoryModel).where(CategoryModel.id == category_id)
        )
        category = queryset.scalars().first()
        return category_model_to_category(category) if category else None

    async def get_list(self):
        queryset = await self._session.execute(sa.select(CategoryModel))
        categories = queryset.scalars().all()
        return [
            category_model_to_category(category) for category in categories
        ]

    async def get_user_categories_list(self, user_id: int) -> list[Category]:
        queryset = await self._session.execute(
            sa.select(CategoryModel).where(CategoryModel.user_id == user_id)
        )
        categories = queryset.scalars().all()
        return [
            category_model_to_category(category) for category in categories
        ]

    async def add(self, category: Category) -> Category:
        self._session.add(category_to_category_model(category))
        await self._session.commit()
        return category

    async def delete(self, category_id: int) -> None:
        await self._session.execute(
            sa.delete(CategoryModel).where(CategoryModel.id == category_id)
        )
        await self._session.commit()
