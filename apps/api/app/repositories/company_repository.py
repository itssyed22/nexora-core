from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate


class CompanyRepository:

    @staticmethod
    def create(db: Session, company: CompanyCreate):

        db_company = Company(
            name=company.name,
            slug=company.slug,
            industry=company.industry,
            company_size=company.company_size,
            country=company.country,
            timezone=company.timezone,
        )

        db.add(db_company)
        db.commit()
        db.refresh(db_company)

        return db_company

    @staticmethod
    def get_all(db: Session):
        return db.query(Company).filter(Company.is_active == True).all()

    @staticmethod
    def get_by_id(db: Session, company_id: int):
        return (
            db.query(Company)
            .filter(
                Company.id == company_id,
                Company.is_active == True
            )
            .first()
        )

    @staticmethod
    def update(db: Session, company_id: int, company: CompanyCreate):

        db_company = (
            db.query(Company)
            .filter(
                Company.id == company_id,
                Company.is_active == True
            )
            .first()
        )

        if not db_company:
            return None

        db_company.name = company.name
        db_company.slug = company.slug
        db_company.industry = company.industry
        db_company.company_size = company.company_size
        db_company.country = company.country
        db_company.timezone = company.timezone

        db.commit()
        db.refresh(db_company)

        return db_company

    @staticmethod
    def delete(db: Session, company_id: int):

        db_company = (
            db.query(Company)
            .filter(
                Company.id == company_id,
                Company.is_active == True
            )
            .first()
        )

        if not db_company:
            return False

        db_company.is_active = False

        db.commit()

        return True