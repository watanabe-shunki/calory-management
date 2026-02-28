from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.orm_entity.orm_entity import Base
from app.infrastructure.db.orm_entity.types import (
    str20
)

class UserORM(Base):
    __tablename__ = "user"
    # TODO: ↓調査
    # DBコメント(メタ情報)
    __table_args__ = {"comment": "User"}

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
        nullable=False,
        comment="User ID(主キー)"
    )

    name: Mapped[str20] = mapped_column(
        nullable=False,
        comment="ユーザー名"
    )