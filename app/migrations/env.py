import asyncio
from logging.config import fileConfig

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import pool

from alembic import context
from models.task import TaskModel
from models.user import UserModel
from models.category import CategoryModel
from core.db import get_postgres_url, Base


config = context.config
config.set_main_option("sqlalchemy.url", get_postgres_url())


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata


async def run_migrations_online():
    connectable = create_async_engine(
        get_postgres_url(), poolclass=pool.NullPool
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def do_run_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
