from datetime import datetime

from pydantic import BaseModel


class KPIUpdateCreate(BaseModel):
    kpi_id: int
    progress: float
    comment: str | None = None


class KPIUpdateResponse(BaseModel):
    id: int
    kpi_id: int
    updated_by: int
    progress: float
    comment: str | None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }