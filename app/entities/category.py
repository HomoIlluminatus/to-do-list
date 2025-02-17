from pydantic import BaseModel


class Category(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None
