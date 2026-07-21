from app.repositories.top_employee_repository import (
    TopEmployeeRepository,
)


class TopEmployeeService:

    @staticmethod
    def get_top_employees(db):

        return TopEmployeeRepository.get_top_employees(db)