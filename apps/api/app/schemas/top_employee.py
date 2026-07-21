from pydantic import BaseModel


class TopEmployeeResponse(BaseModel):
    user_id: int
    employee_name: str

    completed_tasks: int
    completed_kpis: int

    achievement_points: int

    performance_score: float