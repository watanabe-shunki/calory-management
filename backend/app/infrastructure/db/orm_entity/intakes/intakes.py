
from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Date

from backend.app.infrastructure.db.orm_entity.orm_entity import Base
from backend.app.infrastructure.db.orm_entity.types import (
     str2 ,str4, str20
)
from backend.app.infrastructure.db.orm_entity import UsersORM


class IntakeORM(Base):
    __tablename__ = "intakes"

    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    food_name: Mapped[str20] = mapped_column(
        String(20),
        nullable=False,
        comment="食事名"
    )
    calorie: Mapped[str4] = mapped_column(
        String(4),
        nullable=False,
        comment="カロリー"
    )
    protein: Mapped[str2] = mapped_column(
        String(2),
        nullable=False,
        comment="タンパク質"
    )
    date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="日付"
    )
    users: Mapped[UsersORM] = relationship(
        "UsersORM",
        back_populates="intakes",
    )