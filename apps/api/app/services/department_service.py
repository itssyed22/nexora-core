from sqlalchemy.orm import Session

from app.repositories.department_repository import DepartmentRepository
from app.schemas.department import DepartmentCreate


class DepartmentService:

    @staticmethod
    def create_department(
        db: Session,
        department: DepartmentCreate,
    ):
        return DepartmentRepository.create(db, department)

    @staticmethod
    def get_all_departments(
        db: Session,
    ):
        return DepartmentRepository.get_all(db)

    @staticmethod
    def get_department(
        db: Session,
        department_id: int,
    ):
        return DepartmentRepository.get_by_id(
            db,
            department_id,
        )

    @staticmethod
    def delete_department(
        db: Session,
        department_id: int,
    ):
        department = DepartmentRepository.get_by_id(
            db,
            department_id,
        )

        if not department:
            return None

        DepartmentRepository.delete(
            db,
            department,
        )

        return department