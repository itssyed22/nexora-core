from app.models.user import User
from app.core.permissions import require_admin

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.company import CompanyCreate, CompanyResponse
from app.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


@router.post("", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return CompanyService.create_company(db, company)


@router.get("", response_model=list[CompanyResponse])
def get_all_companies(
    db: Session = Depends(get_db),
):
    return CompanyService.get_all_companies(db)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db),
):
    company = CompanyService.get_company_by_id(db, company_id)

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return company


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    company: CompanyCreate,
    db: Session = Depends(get_db),
):
    updated = CompanyService.update_company(
        db,
        company_id,
        company,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return updated


@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db),
):
    deleted = CompanyService.delete_company(
        db,
        company_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    return {
        "message": "Company deleted successfully"
    }