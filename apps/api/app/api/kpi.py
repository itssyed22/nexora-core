from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.permissions import require_admin
from app.database.session import get_db
from app.models.user import User
from app.schemas.kpi import KPICreate, KPIResponse
from app.services.kpi_service import KPIService

router = APIRouter(
    prefix="/kpis",
    tags=["KPIs"],
)


@router.post("", response_model=KPIResponse)
def create_kpi(
    kpi: KPICreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return KPIService.create_kpi(db, kpi)


@router.get("", response_model=list[KPIResponse])
def get_kpis(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return KPIService.get_all_kpis(db)


@router.get("/{kpi_id}", response_model=KPIResponse)
def get_kpi(
    kpi_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    kpi = KPIService.get_kpi(db, kpi_id)

    if not kpi:
        raise HTTPException(
            status_code=404,
            detail="KPI not found",
        )

    return kpi


@router.delete("/{kpi_id}")
def delete_kpi(
    kpi_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    kpi = KPIService.delete_kpi(db, kpi_id)

    if not kpi:
        raise HTTPException(
            status_code=404,
            detail="KPI not found",
        )

    return {
        "message": "KPI deleted successfully"
    }