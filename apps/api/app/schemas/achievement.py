from datetime import datetime

from pydantic import BaseModel


class AchievementCreate(BaseModel):
    user_id: int
    title: str
    description: str | None = None
    category: str = "General"


class AchievementResponse(BaseModel):
    id: int
    user_id: int
    title: str
    description: str | None
    category: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }