from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import get_postgres_url


engine = create_async_engine(url=get_postgres_url(), echo=True)

async_session_factory = sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)


async def get_async_session() -> AsyncSession:  # type: ignore
    async with async_session_factory() as session:
        yield session


Base = declarative_base()
