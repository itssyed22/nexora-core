from app.database.base import Base
from app.database.connection import engine

# Import all models here
from app.models.company import Company


def init_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_database()
    print("✅ Database initialized successfully.")