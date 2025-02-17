from datetime import datetime

from sqlalchemy import String, Enum, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .common import Common
from entities.task import TaskStatus


class TaskModel(Common):
    __tablename__ = "tasks"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(length=100), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    deadline: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), server_default=TaskStatus.WAITING.name
    )
