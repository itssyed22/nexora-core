from sqlalchemy.orm import Session

from app.models.team import Team
from app.schemas.team import TeamCreate


class TeamRepository:

    @staticmethod
    def create(
        db: Session,
        team: TeamCreate,
    ):

        db_team = Team(
            company_id=team.company_id,
            department_id=team.department_id,
            name=team.name,
            description=team.description,
        )

        db.add(db_team)
        db.commit()
        db.refresh(db_team)

        return db_team

    @staticmethod
    def get_all(
        db: Session,
    ):

        return (
            db.query(Team)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        team_id: int,
    ):

        return (
            db.query(Team)
            .filter(Team.id == team_id)
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        team: Team,
    ):

        db.delete(team)
        db.commit()
        