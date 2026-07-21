from pydantic import BaseModel


class KPITrendResponse(BaseModel):
    total: int
    completed: int
    in_progress: int
    not_started: int