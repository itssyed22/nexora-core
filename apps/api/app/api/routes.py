from fastapi import APIRouter
from app.api.department import router as department_router
from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.company import router as company_router
from app.api.user import router as user_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(health_router)
router.include_router(company_router)
router.include_router(user_router)

router.include_router(department_router)