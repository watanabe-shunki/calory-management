from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey
from streamlit.elements.lib.utils import compute_and_register_element_id

from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.types import (
    str3, str10
)
from app.infrastructure.db.orm_entity.daily_records.deily_records import DailyRecords



class ExercisesORM(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    daily_unit_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("daily_records.id", ondelete="CASCADE"),
        nullable=False,
        comment="日単位のデータのID"
    )
    exercise_name: Mapped[str10] = mapped_column(
        String,
        nullable=False,
        comment="運動名"
    )
    calories_burned: Mapped[str3] = mapped_column(
        String,
        nullable=False,
        comment="消費カロリー"
    )
    daily_records: Mapped[DailyRecords] = relationship(
        back_populates="exercises",
        cascade="all, delete-orphan"
    )