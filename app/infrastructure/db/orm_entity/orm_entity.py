from sqlalchemy.orm import DeclarativeBase

from app.infrastructure.db.orm_entity.types import TYPE_ANNOTATION_MAP


class Base(DeclarativeBase):
    type_annotation_map = TYPE_ANNOTATION_MAP

