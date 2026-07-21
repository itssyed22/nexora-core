from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.dashboard import DashboardSummary

from app.services.dashboard_service import DashboardService

from app.core.auth import get_current_user


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/summary",
    response_model=DashboardSummary,
)
def get_dashboard_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DashboardService.get_summary(db)


@router.get("/recent-tasks")
def get_recent_tasks(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return DashboardService.get_recent_tasks(db)