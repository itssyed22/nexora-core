from sqlalchemy.orm import Session

from app.repositories.company_repository import CompanyRepository
from app.schemas.company import CompanyCreate


class CompanyService:

    @staticmethod
    def create_company(db: Session, company: CompanyCreate):
        return CompanyRepository.create(db, company)

    @staticmethod
    def get_all_companies(db: Session):
        return CompanyRepository.get_all(db)

    @staticmethod
    def get_company_by_id(db: Session, company_id: int):
        return CompanyRepository.get_by_id(db, company_id)

    @staticmethod
    def update_company(db: Session, company_id: int, company: CompanyCreate):
        return CompanyRepository.update(db, company_id, company)

    @staticmethod
    def delete_company(db: Session, company_id: int):
        return CompanyRepository.delete(db, company_id)