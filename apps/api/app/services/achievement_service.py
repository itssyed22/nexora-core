from app.models.achievement import Achievement
from app.repositories.achievement_repository import AchievementRepository


class AchievementService:

    @staticmethod
    def create_achievement(db, achievement_data):

        achievement = Achievement(**achievement_data.model_dump())

        return AchievementRepository.create(db, achievement)

    @staticmethod
    def get_all_achievements(db):
        return AchievementRepository.get_all(db)

    @staticmethod
    def get_achievement(db, achievement_id):
        return AchievementRepository.get_by_id(db, achievement_id)

    @staticmethod
    def delete_achievement(db, achievement_id):

        achievement = AchievementRepository.get_by_id(
            db,
            achievement_id,
        )

        if not achievement:
            return None

        AchievementRepository.delete(db, achievement)

        return achievement