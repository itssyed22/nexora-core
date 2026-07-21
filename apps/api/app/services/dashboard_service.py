from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    @staticmethod
    def get_summary(db):
        return DashboardRepository.get_summary(db)

    @staticmethod
    def get_recent_tasks(db):
        return DashboardRepository.get_recent_tasks(db)