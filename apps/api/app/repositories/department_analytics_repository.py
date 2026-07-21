from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.department import Department
from app.models.kpi import KPI


class DepartmentAnalyticsRepository:

    @staticmethod
    def get_department_performance(db: Session):

        departments = db.query(Department).all()

        results = []

        for department in departments:

            total = (
                db.query(KPI)
                .filter(KPI.department_id == department.id)
                .count()
            )

            completed = (
                db.query(KPI)
                .filter(
                    KPI.department_id == department.id,
                    KPI.status == "Completed",
                )
                .count()
            )

            rate = 0

            if total > 0:
                rate = round((completed / total) * 100, 2)

            results.append(
                {
                    "department": department.name,
                    "total_kpis": total,
                    "completed_kpis": completed,
                    "completion_rate": rate,
                }
            )

        return results