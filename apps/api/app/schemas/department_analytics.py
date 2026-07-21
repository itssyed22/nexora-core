from pydantic import BaseModel


class DepartmentPerformance(BaseModel):
    department: str
    total_kpis: int
    completed_kpis: int
    completion_rate: float