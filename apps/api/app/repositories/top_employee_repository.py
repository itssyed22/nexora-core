from sqlalchemy.orm import Session

from app.models.user import User
from app.models.task import Task
from app.models.kpi import KPI
from app.models.achievement import Achievement


class TopEmployeeRepository:

    @staticmethod
    def get_top_employees(db: Session):

        employees = db.query(User).all()

        result = []

        for employee in employees:

            completed_tasks = (
                db.query(Task)
                .filter(
                    Task.assigned_user_id == employee.id,
                    Task.status == "Completed",
                )
                .count()
            )

            completed_kpis = (
                db.query(KPI)
                .filter(
                    KPI.assigned_user_id == employee.id,
                    KPI.status == "Completed",
                )
                .count()
            )

            achievements = (
                db.query(Achievement)
                .filter(
                    Achievement.user_id == employee.id
                )
                .all()
            )

            achievement_points = sum(a.points for a in achievements)

            performance_score = (
                completed_tasks * 10
                + completed_kpis * 20
                + achievement_points
            )

            result.append(
                {
                    "user_id": employee.id,
                    "employee_name": f"{employee.first_name} {employee.last_name}",
                    "completed_tasks": completed_tasks,
                    "completed_kpis": completed_kpis,
                    "achievement_points": achievement_points,
                    "performance_score": performance_score,
                }
            )

        result.sort(
            key=lambda x: x["performance_score"],
            reverse=True,
        )

        return result