from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import select
from dataclasses import dataclass

from app.domain.body_info.value_object.get_body_info import BodyInfo
from app.domain.user.value_object.get_user_name import UserId
from app.domain.body_info.enums.activity_level import ActivityStatus
from app.usecase.get_height_weight_info.height_weight_info_Query_Service import AbstractsGetHeightWeightInfoQueryService
from app.infrastructure.db.orm_entity.body_profiles.body_profiles import BodyProfilesORM
from app.infrastructure.db.orm_entity.users.users import UsersORM


class HeightWeightInfoQueryService(AbstractsGetHeightWeightInfoQueryService):
    def __init__(
        self,
        db_session: Session
    ):
        self.db_session = db_session

    def get_height_weight_info(
            self,
            user_id: UserId,
    ) -> BodyInfo:
        print(user_id, type(user_id))
        print(
            self.db_session.execute(
                select(BodyProfilesORM)
            ).all()
        )
        try:
            query =(
                select(
                    BodyProfilesORM.height,
                    BodyProfilesORM.weight_kg,
                    BodyProfilesORM.activity_status
                )
                .where(BodyProfilesORM.user_id == user_id.value) # UserId型の変数なので、int型のBodyProfilesORM.user_idと一致しない。そのため.valueを行う。
                .order_by(BodyProfilesORM.recorded_at.desc())
                .limit(1)
            )
            # print(
            #     self.db_session.execute(
            #         select(f"身体情報取得 :{BodyProfilesORM}")
            #     ).all()
            # )
            result = self.db_session.execute(query).first()

            if result is None:
                raise HTTPException(status_code=404, detail="身体情報が存在しません")

            height, weight, activity_status = result

            return BodyInfo(
                height=height,
                weight=weight,
                activity_status=ActivityStatus(activity_status)
            )
        except SQLAlchemyError:
            raise HTTPException(status_code=500, detail="DBエラー")
