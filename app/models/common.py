from datetime import datetime

from sqlalchemy import TIMESTAMP, func, Integer
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class Common(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP, server_default=func.now, onupdate=func.now
    )
