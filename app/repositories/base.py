from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from sqlalchemy.ext.asyncio import AsyncSession


Entity = TypeVar("Entity")


class BaseRepository(ABC, Generic[Entity]):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    @abstractmethod
    async def get_by_id(self, entity_id: int) -> Entity | None: ...

    @abstractmethod
    async def get_list(self) -> list[Entity]: ...

    @abstractmethod
    async def add(self, entity: Entity) -> Entity: ...

    @abstractmethod
    async def delete(self, entity_id: int) -> None: ...
