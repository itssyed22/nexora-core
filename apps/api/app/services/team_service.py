from sqlalchemy.orm import Session

from app.repositories.team_repository import TeamRepository
from app.schemas.team import TeamCreate


class TeamService:

    @staticmethod
    def create_team(
        db: Session,
        team: TeamCreate,
    ):
        return TeamRepository.create(db, team)

    @staticmethod
    def get_all_teams(
        db: Session,
    ):
        return TeamRepository.get_all(db)

    @staticmethod
    def get_team(
        db: Session,
        team_id: int,
    ):
        return TeamRepository.get_by_id(
            db,
            team_id,
        )

    @staticmethod
    def delete_team(
        db: Session,
        team_id: int,
    ):
        team = TeamRepository.get_by_id(
            db,
            team_id,
        )

        if not team:
            return None

        TeamRepository.delete(
            db,
            team,
        )

        return team