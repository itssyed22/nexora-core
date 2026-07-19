from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    company_id: int
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str = "employee"


class UserResponse(BaseModel):
    id: int
    company_id: int
    first_name: str
    last_name: str
    email: EmailStr
    role: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }