from sqlalchemy.orm import Session

from app.models.achievement import Achievement


class AchievementRepository:

    @staticmethod
    def create(db: Session, achievement: Achievement):
        db.add(achievement)
        db.commit()
        db.refresh(achievement)
        return achievement

    @staticmethod
    def get_all(db: Session):
        return db.query(Achievement).all()

    @staticmethod
    def get_by_id(db: Session, achievement_id: int):
        return (
            db.query(Achievement)
            .filter(Achievement.id == achievement_id)
            .first()
        )

    @staticmethod
    def delete(db: Session, achievement: Achievement):
        db.delete(achievement)
        db.commit()