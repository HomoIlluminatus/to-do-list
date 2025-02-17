from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session


Entity = TypeVar("Entity")


class BaseRepository(ABC, Generic[Entity]):
    def __init__(
        self, session: AsyncSession = Depends(get_async_session)
    ) -> None:
        self._session = session

    @abstractmethod
    async def get_by_id(self, entity_id: int) -> Entity | None: ...

    @abstractmethod
    async def get_list(self) -> list[Entity]: ...

    @abstractmethod
    async def add(self, entity: Entity) -> Entity: ...

    @abstractmethod
    async def delete(self, entity_id: int) -> None: ...
