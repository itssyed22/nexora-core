from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("companies.id"),
        nullable=False,
    )

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False,
    )

    assigned_user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default="Medium",
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="Pending",
    )

    estimated_hours: Mapped[float] = mapped_column(
    default=0,
    )

    actual_hours: Mapped[float] = mapped_column(
    default=0,
    )

    progress_percentage: Mapped[float] = mapped_column(
    default=0,
    )

    due_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    start_date: Mapped[date] = mapped_column(
    Date,
    nullable=False,
    )

    completed_at: Mapped[datetime | None] = mapped_column(
    DateTime,
    nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
    DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow,
    )