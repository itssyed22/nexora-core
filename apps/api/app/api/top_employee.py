from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.top_employee import TopEmployeeResponse
from app.services.top_employee_service import TopEmployeeService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Analytics"],
)


@router.get(
    "/top-employees",
    response_model=list[TopEmployeeResponse],
)
def get_top_employees(
    db: Session = Depends(get_db),
):
    return TopEmployeeService.get_top_employees(db)