from datetime import date
from sqlalchemy import Integer, String, ForeignKey, Date, func, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.types import (
    str3
)
from app.domain.body_info.enums.activity_level import ActivityStatus


class BodyProfiles(Base):
    __tablename__ = "body_profiles"

    __table_args__ = {"comment": "ユーザー身体情報"}

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        nullable=False,
        comment="主キー"
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        ondelete="CASCADE"
    )
    height: Mapped[str3] = mapped_column(
        String,
        nullable=False,
        comment="身長"
    )
    weight_kg: Mapped[str3] = mapped_column(
        String,
        nullable=False,
        comment="体重"
    )
    activity_status: Mapped[ActivityStatus] = mapped_column(
        Enum(ActivityStatus, name="activity_status"),
        nullable=False,
        comment="生活レベル"
    )
    recorded_at: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        server_default=func.current_date(),
        comment="登録日"
    )