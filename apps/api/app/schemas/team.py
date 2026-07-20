from pydantic import BaseModel


class TeamCreate(BaseModel):
    company_id: int
    department_id: int
    name: str
    description: str | None = None


class TeamResponse(BaseModel):
    id: int
    company_id: int
    department_id: int
    name: str
    description: str | None
    is_active: bool

    model_config = {
        "from_attributes": True
    }