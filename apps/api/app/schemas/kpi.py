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

    weight: int = 1
    progress_percentage: float = 0
    score: float = 0


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

    weight: int
    progress_percentage: float
    score: float

    model_config = {
        "from_attributes": True
    }