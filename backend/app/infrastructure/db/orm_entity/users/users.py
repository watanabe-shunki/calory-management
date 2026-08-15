from datetime import datetime
from tokenize import String

from sqlalchemy import Integer, String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.infrastructure.db.orm_entity.types import str10, str30, str255
from backend.app.infrastructure.db.orm_entity.orm_entity import Base


class UsersORM(Base):
    __tablename__ = "users"

    __table_args__ = {"comment": "users"}

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    email: Mapped[str30] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash: Mapped[str255 | None] = mapped_column(
        String(255),
        nullable=True
    )

    google_id: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True,
    )

    name: Mapped[str30] = mapped_column(
        String(20),
        nullable=False,
    )

    auth_provider: Mapped[str10] = mapped_column(
        String(10),
        nullable=False,
        comment="googleか通常かのステータスを保持する",
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    last_login_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
    )

    body_profiles = relationship(
        "BodyProfilesORM",
        back_populates="users",
        cascade="all, delete-orphan"
    )

    goals = relationship(
        "GoalsORM",
        back_populates="users",
        cascade="all, delete-orphan"
    )

    intakes = relationship(
        "IntakeORM",
        back_populates="users",
        cascade="all, delete-orphan"
    )

    exercises = relationship(
        "ExercisesORM",
        back_populates="users",
        cascade="all, delete-orphan"
    )