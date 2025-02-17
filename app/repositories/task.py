from abc import abstractmethod

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from core.db import get_async_session
from .base import BaseRepository
from .mappers import task_model_to_task, task_to_task_model
from entities.task import Task
from models.task import TaskModel


class AbstractTaskRepository(BaseRepository[Task]):
    @abstractmethod
    async def get_user_tasks_list(self, user_id: int) -> list[Task]: ...

    @abstractmethod
    async def get_category_tasks_list(
        self, category_id: int
    ) -> list[Task]: ...


class TaskRepository(AbstractTaskRepository):
    def __init__(
        self, session: AsyncSession = Depends(get_async_session)
    ) -> None:
        super().__init__(session)

    async def get_by_id(self, task_id: int) -> Task | None:
        queryset = await self._session.execute(
            sa.select(TaskModel).where(TaskModel.id == task_id)
        )
        task = queryset.scalars().first()
        return task_model_to_task(task) if task else None

    async def get_list(self) -> list[Task]:
        queryset = await self._session.execute(sa.select(TaskModel))
        tasks = queryset.scalars().all()
        return [task_model_to_task(task) for task in tasks]

    async def get_user_tasks_list(self, user_id) -> list[Task]:
        queryset = await self._session.execute(
            sa.select(TaskModel).where(TaskModel.user_id == user_id)
        )
        tasks = queryset.scalars().all()
        return [task_model_to_task(task) for task in tasks]

    async def get_category_tasks_list(self, category_id) -> list[Task]:
        queryset = await self._session.execute(
            sa.select(TaskModel).where(TaskModel.category_id == category_id)
        )
        tasks = queryset.scalars().all()
        return [task_model_to_task(task) for task in tasks]

    async def add(self, task) -> Task:
        self._session.add(task_to_task_model(task))
        await self._session.commit()
        return task

    async def delete(self, task_id) -> None:
        await self._session.execute(
            sa.delet(TaskModel).where(TaskModel.id == task_id)
        )
        await self._session.commit()
