from sqlalchemy.orm import Session

from app.models.kpi import KPI
from app.schemas.kpi import KPICreate


class KPIRepository:

    @staticmethod
    def create(
        db: Session,
        kpi: KPICreate,
    ):
        db_kpi = KPI(
            company_id=kpi.company_id,
            department_id=kpi.department_id,
            team_id=kpi.team_id,
            assigned_user_id=kpi.assigned_user_id,
            title=kpi.title,
            description=kpi.description,
            target_value=kpi.target_value,
            current_value=kpi.current_value,
            unit=kpi.unit,
            status=kpi.status,
            priority=kpi.priority,
            start_date=kpi.start_date,
            due_date=kpi.due_date,
        )

        db.add(db_kpi)
        db.commit()
        db.refresh(db_kpi)

        return db_kpi

    @staticmethod
    def get_all(db: Session):
        return db.query(KPI).all()

    @staticmethod
    def get_by_id(
        db: Session,
        kpi_id: int,
    ):
        return (
            db.query(KPI)
            .filter(KPI.id == kpi_id)
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        kpi: KPI,
    ):
        db.delete(kpi)
        db.commit()