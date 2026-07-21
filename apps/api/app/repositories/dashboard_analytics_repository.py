from sqlalchemy.orm import Session

from app.models.kpi import KPI


class DashboardAnalyticsRepository:

    @staticmethod
    def get_kpi_trends(db: Session):

        total = db.query(KPI).count()

        completed = (
            db.query(KPI)
            .filter(KPI.status == "Completed")
            .count()
        )

        in_progress = (
            db.query(KPI)
            .filter(KPI.status == "In Progress")
            .count()
        )

        not_started = (
            db.query(KPI)
            .filter(KPI.status == "Not Started")
            .count()
        )

        return {
            "total": total,
            "completed": completed,
            "in_progress": in_progress,
            "not_started": not_started,
        }