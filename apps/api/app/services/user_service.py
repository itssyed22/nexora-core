from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:

    @staticmethod
    def create_user(db: Session, user_data: UserCreate):

        existing = UserRepository.get_by_email(
            db,
            user_data.email
        )

        if existing:
            raise ValueError("Email already exists.")

        user = User(
            company_id=user_data.company_id,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            role=user_data.role,
            is_active=True,
        )

        return UserRepository.create(db, user)

    @staticmethod
    def get_all_users(db: Session):
        return UserRepository.get_all(db)

    @staticmethod
    def get_user(db: Session, user_id: int):
        return UserRepository.get_by_id(db, user_id)

    @staticmethod
    def delete_user(db: Session, user_id: int):

        user = UserRepository.get_by_id(db, user_id)

        if not user:
            return None

        UserRepository.delete(db, user)
        return user