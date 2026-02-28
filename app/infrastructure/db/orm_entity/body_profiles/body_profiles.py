from datetime import date
from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.types import (
    str3, str20
)


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
    activity_level: Mapped[str20] = mapped_column(
        String,
        nullable=False,
        comment="生活レベル"
    )
    recorded_at: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        comment="登録日"
    )