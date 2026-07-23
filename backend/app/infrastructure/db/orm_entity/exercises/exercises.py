from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date
from backend.app.infrastructure.db.orm_entity.orm_entity import Base
from backend.app.infrastructure.db.orm_entity.types import (
    str3, str10
)
from backend.app.infrastructure.db.orm_entity import UsersORM


class ExercisesORM(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    exercise_name: Mapped[str10] = mapped_column(
        String(10),
        nullable=False,
        comment="運動名"
    )
    calories_burned: Mapped[str3] = mapped_column(
        String(3),
        nullable=False,
        comment="消費カロリー"
    )
    date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="日付"
    )
    users: Mapped[UsersORM] = relationship(
        "UsersORM",
        back_populates="exercises",
    )