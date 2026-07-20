from datetime import date

from pydantic import BaseModel


class KPICreate(BaseModel):
    company_id: int
    department_id: int
    team_id: int
    assigned_user_id: int

    title: str
    description: str | None = None

    target_value: float
    current_value: float = 0

    unit: str = "%"

    status: str = "Not Started"
    priority: str = "Medium"

    start_date: date
    due_date: date


class KPIResponse(BaseModel):
    id: int

    company_id: int
    department_id: int
    team_id: int
    assigned_user_id: int

    title: str
    description: str | None

    target_value: float
    current_value: float

    unit: str

    status: str
    priority: str

    start_date: date
    due_date: date

    model_config = {
        "from_attributes": True
    }