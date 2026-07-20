from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.achievement import (
    AchievementCreate,
    AchievementResponse,
)
from app.services.achievement_service import AchievementService

router = APIRouter(
    prefix="/achievements",
    tags=["Achievements"],
)


@router.post("", response_model=AchievementResponse)
def create_achievement(
    achievement: AchievementCreate,
    db: Session = Depends(get_db),
):
    return AchievementService.create_achievement(db, achievement)


@router.get("", response_model=list[AchievementResponse])
def get_all_achievements(
    db: Session = Depends(get_db),
):
    return AchievementService.get_all_achievements(db)


@router.get("/{achievement_id}", response_model=AchievementResponse)
def get_achievement(
    achievement_id: int,
    db: Session = Depends(get_db),
):

    achievement = AchievementService.get_achievement(
        db,
        achievement_id,
    )

    if not achievement:
        raise HTTPException(
            status_code=404,
            detail="Achievement not found",
        )

    return achievement


@router.delete("/{achievement_id}")
def delete_achievement(
    achievement_id: int,
    db: Session = Depends(get_db),
):

    achievement = AchievementService.delete_achievement(
        db,
        achievement_id,
    )

    if not achievement:
        raise HTTPException(
            status_code=404,
            detail="Achievement not found",
        )

    return {
        "message": "Achievement deleted successfully"
    }