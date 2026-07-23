from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.infrastructure.db.orm_entity.orm_entity import Base


class UsersORM(Base):
    __tablename__ = "users"

    __table_args__ = {"comment": "users"}

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
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