from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class TaskStatus(Enum):
    WAITING = "waiting"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


class Task(BaseModel):
    id: int
    user_id: int
    category_id: int
    title: str
    description: str | None
    deadline: datetime | None
    status: TaskStatus = TaskStatus.WAITING
