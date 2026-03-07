from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.types import (
    str3, str4
)


class GoalsORM(Base):
    __tablename__ = 'goals'
    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
    )
    user_id: Mapped[int] = mapped_column(
        String,
        ForeignKey("users.id"),
        nullable=False,
        ondelete= "CASCADE"
    )
    basal_calories: Mapped[str4] = mapped_column(
        String,
        nullable=False,
        comment="基礎代謝"
    )
    deficit: Mapped[str4] = mapped_column(
        String,
        nullable=False,
        comment="赤字カロリー"
    )
    protein: Mapped[str3] = mapped_column(
        String,
        nullable=False,
        comment="タンパク質"
    )
