from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.db.orm_entity.orm_entity import Base


class UserORM(Base):
    __tablename__ = "users"

    __table_args__ = {"comment": "users"}

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )