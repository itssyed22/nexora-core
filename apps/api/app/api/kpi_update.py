from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.database.session import get_db
from app.models.user import User
from app.schemas.kpi_update import (
    KPIUpdateCreate,
    KPIUpdateResponse,
)
from app.services.kpi_update_service import KPIUpdateService

router = APIRouter(
    prefix="/kpi-updates",
    tags=["KPI Updates"],
)


@router.post(
    "",
    response_model=KPIUpdateResponse,
)
def create_update(
    update: KPIUpdateCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return KPIUpdateService.create_update(
        db,
        update,
        current_user.id,
    )


@router.get(
    "/{kpi_id}",
    response_model=list[KPIUpdateResponse],
)
def get_updates(
    kpi_id: int,
    db: Session = Depends(get_db),
):
    return KPIUpdateService.get_updates(
        db,
        kpi_id,
    )