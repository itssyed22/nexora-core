from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.department_analytics import DepartmentPerformance
from app.services.department_analytics_service import (
    DepartmentAnalyticsService,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Analytics"],
)


@router.get(
    "/department-performance",
    response_model=list[DepartmentPerformance],
)
def get_department_performance(
    db: Session = Depends(get_db),
):
    return DepartmentAnalyticsService.get_department_performance(db)