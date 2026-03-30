from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from dataclasses import dataclass

from app.domain.user.value_object.get_user_name import UserName, UserId
from app.usecase.get_user.user_Query_Service import AbstractGetUserNameQueryService
from app.infrastructure.db.orm_entity.users.users import UsersORM


@dataclass
class UserNameDTO:
    name: UserName

# 実施にDBテーブル作成作成していないので後日実施
class UserNameQueryService(AbstractGetUserNameQueryService):
    def __init__(
        self,
        db_session: Session
    ):
        self.db_session = db_session

    def get_user_name(
            self,
            user_id: UserId
    ) -> UserName:
        try:
            query = (
                select(UsersORM.id)
                .where(UsersORM.id == user_id.value)
            )
            result = self.db_session.scalar(query)

            return UserId(result)
        except:
            raise HTTPException(status_code=500, detail="Server Error")