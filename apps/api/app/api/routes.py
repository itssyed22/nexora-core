from fastapi import APIRouter
from app.api.department import router as department_router
from app.api.auth import router as auth_router
from app.api.health import router as health_router
from app.api.company import router as company_router
from app.api.user import router as user_router
from app.api.team import router as team_router
from app.api.kpi import router as kpi_router
from app.api.kpi_update import router as kpi_update_router
from app.api.achievement import router as achievement_router
from app.api.task import router as task_router
from app.api.dashboard import router as dashboard_router
from app.api.dashboard_analytics import router as dashboard_analytics_router
from app.api.department_analytics import (
    router as department_analytics_router,
)
from app.api.top_employee import router as top_employee_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(health_router)
router.include_router(company_router)
router.include_router(user_router)
router.include_router(achievement_router)
router.include_router(department_router)

router.include_router(team_router)

router.include_router(kpi_router)
router.include_router(kpi_update_router)

router.include_router(task_router)
router.include_router(dashboard_router)
router.include_router(dashboard_analytics_router)
router.include_router(department_analytics_router)
router.include_router(top_employee_router)