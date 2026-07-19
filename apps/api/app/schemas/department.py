from pydantic import BaseModel


class DepartmentCreate(BaseModel):
    company_id: int
    name: str
    description: str | None = None


class DepartmentResponse(BaseModel):
    id: int
    company_id: int
    name: str
    description: str | None
    is_active: bool

    model_config = {
        "from_attributes": True
    }