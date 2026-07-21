from app.repositories.department_analytics_repository import (
    DepartmentAnalyticsRepository,
)


class DepartmentAnalyticsService:

    @staticmethod
    def get_department_performance(db):

        return (
            DepartmentAnalyticsRepository
            .get_department_performance(db)
        )