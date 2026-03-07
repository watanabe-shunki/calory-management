from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.types import (
     str2,str3 ,str4, str20
)
from app.infrastructure.db.orm_entity.daily_records.deily_records import DailyRecords


class IntakeORM(Base):
    __tablename__ = "intakes"

    id: Mapped[int] = mapped_column(
        Integer,
        autoincrement=True,
        primary_key=True
    )
    daily_unit_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("daily_records.id", ondelete="CASCADE"),
        nullable=False,
        comment="日単位のデータのID"
    )
    food_name: Mapped[str20] = mapped_column(
        String,
        nullable=False,
        comment="食事名"
    )
    calorie: Mapped[str4] = mapped_column(
        String,
        nullable=False,
        comment="カロリー"
    )
    protein: Mapped[str2] = mapped_column(
        String,
        nullable=False,
        comment="タンパク質"
    )
    daily_records: Mapped[DailyRecords] = relationship(
        back_populates="intakes",
        cascade="all, delete-orphan"
    )