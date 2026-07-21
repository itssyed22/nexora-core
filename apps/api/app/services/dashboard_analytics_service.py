from app.repositories.dashboard_analytics_repository import (
    DashboardAnalyticsRepository,
)


class DashboardAnalyticsService:

    @staticmethod
    def get_kpi_trends(db):

        return DashboardAnalyticsRepository.get_kpi_trends(db)