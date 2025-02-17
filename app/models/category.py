from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .common import Common


class CategoryModel(Common):
    __tablename__ = "categories"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
