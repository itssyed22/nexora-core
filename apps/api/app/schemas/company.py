from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name: str
    slug: str
    industry: Optional[str] = None
    company_size: Optional[str] = None
    country: Optional[str] = None
    timezone: Optional[str] = None


class CompanyResponse(CompanyCreate):
    id: int
    is_active: bool

    class Config:
        from_attributes = True