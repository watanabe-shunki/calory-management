from datetime import date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, Integer, ForeignKey, UniqueConstraint, Index
from typing import List
from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.intakes.intakes import Intake
from app.infrastructure.db.orm_entity.exercises.exercises import Exercises


class DailyRecordsORM(Base):
    __tablename__ = "daily_records"
    id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        autoincrement=True,
        primary_key=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        comment="ユーザーID"
    )
    date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="日付"
    )
    # 食事情報
    intakes: Mapped[List["Intake"]] = relationship(
        back_populates="daily_records",
        cascade="all, delete-orphan"
    )
    # 運動情報
    exercises: Mapped[List["Exercises"]] = relationship(
        back_populates="daily_records",
        cascade="all, delete-orphan"
    )
    """
    一意の制約を定義
    同じ日付レコード重複防止
    """
    __table_args__ = (
        UniqueConstraint("user_id", "date", name="uq_user_date"),
        Index("ix_user_date", "user_id", "date"),
    )