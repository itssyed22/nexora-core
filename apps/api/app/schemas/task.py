from datetime import date, datetime

from pydantic import BaseModel


class TaskCreate(BaseModel):
    company_id: int
    department_id: int
    assigned_user_id: int
    title: str
    description: str | None = None
    priority: str = "Medium"
    status: str = "Pending"
    due_date: date


class TaskResponse(BaseModel):
    id: int
    company_id: int
    department_id: int
    assigned_user_id: int
    title: str
    description: str | None
    priority: str
    status: str
    due_date: date
    created_at: datetime

    model_config = {
        "from_attributes": True
    }