from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class KPIUpdate(Base):
    __tablename__ = "kpi_updates"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    kpi_id: Mapped[int] = mapped_column(
        ForeignKey("kpis.id"),
        nullable=False,
    )

    updated_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    progress: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    comment: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )