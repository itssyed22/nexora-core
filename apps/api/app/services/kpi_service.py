from sqlalchemy.orm import Session

from app.repositories.kpi_repository import KPIRepository
from app.schemas.kpi import KPICreate


class KPIService:

    @staticmethod
    def create_kpi(
        db: Session,
        kpi: KPICreate,
    ):
        return KPIRepository.create(db, kpi)

    @staticmethod
    def get_all_kpis(
        db: Session,
    ):
        return KPIRepository.get_all(db)

    @staticmethod
    def get_kpi(
        db: Session,
        kpi_id: int,
    ):
        return KPIRepository.get_by_id(
            db,
            kpi_id,
        )

    @staticmethod
    def delete_kpi(
        db: Session,
        kpi_id: int,
    ):
        kpi = KPIRepository.get_by_id(
            db,
            kpi_id,
        )

        if not kpi:
            return None

        KPIRepository.delete(
            db,
            kpi,
        )

        return kpi