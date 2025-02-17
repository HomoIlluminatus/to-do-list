from abc import abstractmethod

from .base import BaseRepository
from entities.task import Task


class AbstractTaskRepository(BaseRepository[Task]):
    @abstractmethod
    async def get_user_tasks_list(self, user_id: int) -> list[Task]: ...

    @abstractmethod
    async def get_category_tasks_list(
        self, category_id: int
    ) -> list[Task]: ...
