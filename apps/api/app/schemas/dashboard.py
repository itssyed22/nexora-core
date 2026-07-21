from pydantic import BaseModel


class DashboardSummary(BaseModel):
    total_users: int
    total_departments: int
    total_teams: int
    total_kpis: int

    completed_kpis: int
    in_progress_kpis: int
    pending_kpis: int

    total_tasks: int
    completed_tasks: int
    pending_tasks: int

    total_achievements: int