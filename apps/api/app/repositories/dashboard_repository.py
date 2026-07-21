from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.department import Department
from app.models.team import Team
from app.models.kpi import KPI
from app.models.task import Task
from app.models.achievement import Achievement


class DashboardRepository:

    @staticmethod
    def get_summary(db: Session):

        return {

            "total_users":
                db.query(func.count(User.id)).scalar(),

            "total_departments":
                db.query(func.count(Department.id)).scalar(),

            "total_teams":
                db.query(func.count(Team.id)).scalar(),

            "total_kpis":
                db.query(func.count(KPI.id)).scalar(),

            "completed_kpis":
                db.query(KPI).filter(
                    KPI.status == "Completed"
                ).count(),

            "in_progress_kpis":
                db.query(KPI).filter(
                    KPI.status == "In Progress"
                ).count(),

            "pending_kpis":
                db.query(KPI).filter(
                    KPI.status == "Not Started"
                ).count(),

            "total_tasks":
                db.query(func.count(Task.id)).scalar(),

            "completed_tasks":
                db.query(Task).filter(
                    Task.status == "Completed"
                ).count(),

            "pending_tasks":
                db.query(Task).filter(
                    Task.status == "Pending"
                ).count(),

            "total_achievements":
                db.query(func.count(Achievement.id)).scalar(),
        }

    @staticmethod
    def get_recent_tasks(db: Session):

        tasks = (
            db.query(Task)
            .order_by(Task.created_at.desc())
            .limit(5)
            .all()
        )

        return [
            {
                "id": task.id,
                "title": task.title,
                "priority": task.priority,
                "status": task.status,
                "due_date": task.due_date,
            }
            for task in tasks
        ]