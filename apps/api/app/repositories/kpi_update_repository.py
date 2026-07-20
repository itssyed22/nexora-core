from sqlalchemy.orm import Session

from app.models.kpi import KPI
from app.models.kpi_update import KPIUpdate
from app.schemas.kpi_update import KPIUpdateCreate


class KPIUpdateRepository:

    @staticmethod
    def create(
        db: Session,
        update: KPIUpdateCreate,
        user_id: int,
    ):

        db_update = KPIUpdate(
            kpi_id=update.kpi_id,
            updated_by=user_id,
            progress=update.progress,
            comment=update.comment,
        )

        db.add(db_update)

        kpi = (
            db.query(KPI)
            .filter(KPI.id == update.kpi_id)
            .first()
        )

        if kpi:
            kpi.current_value = update.progress

            if update.progress >= kpi.target_value:
                kpi.status = "Completed"
            elif update.progress > 0:
                kpi.status = "In Progress"

        db.commit()
        db.refresh(db_update)

        return db_update

    @staticmethod
    def get_by_kpi(
        db: Session,
        kpi_id: int,
    ):

        return (
            db.query(KPIUpdate)
            .filter(KPIUpdate.kpi_id == kpi_id)
            .order_by(KPIUpdate.created_at.desc())
            .all()
        )