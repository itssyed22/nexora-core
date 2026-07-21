from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.dashboard_analytics import KPITrendResponse
from app.services.dashboard_analytics_service import DashboardAnalyticsService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard Analytics"],
)


@router.get(
    "/kpi-trends",
    response_model=KPITrendResponse,
)
def get_kpi_trends(
    db: Session = Depends(get_db),
):
    return DashboardAnalyticsService.get_kpi_trends(db)