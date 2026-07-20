from sqlalchemy.orm import Session

from app.repositories.kpi_update_repository import KPIUpdateRepository
from app.schemas.kpi_update import KPIUpdateCreate


class KPIUpdateService:

    @staticmethod
    def create_update(
        db: Session,
        update: KPIUpdateCreate,
        user_id: int,
    ):
        return KPIUpdateRepository.create(
            db,
            update,
            user_id,
        )

    @staticmethod
    def get_updates(
        db: Session,
        kpi_id: int,
    ):
        return KPIUpdateRepository.get_by_kpi(
            db,
            kpi_id,
        )