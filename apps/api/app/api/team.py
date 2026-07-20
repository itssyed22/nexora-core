from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.permissions import require_admin
from app.database.session import get_db
from app.models.user import User
from app.schemas.team import TeamCreate, TeamResponse
from app.services.team_service import TeamService

router = APIRouter(
    prefix="/teams",
    tags=["Teams"],
)


@router.post("", response_model=TeamResponse)
def create_team(
    team: TeamCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return TeamService.create_team(db, team)


@router.get("", response_model=list[TeamResponse])
def get_teams(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return TeamService.get_all_teams(db)


@router.get("/{team_id}", response_model=TeamResponse)
def get_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    team = TeamService.get_team(db, team_id)

    if not team:
        raise HTTPException(
            status_code=404,
            detail="Team not found",
        )

    return team


@router.delete("/{team_id}")
def delete_team(
    team_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    team = TeamService.delete_team(db, team_id)

    if not team:
        raise HTTPException(
            status_code=404,
            detail="Team not found",
        )

    return {
        "message": "Team deleted successfully"
    }