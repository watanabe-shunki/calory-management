from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from dataclasses import dataclass

from app.domain.body_info.value_object.get_body_info import BodyInfo
from app.domain.user.value_object.get_user_name import UserId
from app.usecase.get_height_weight_info.height_weight_info_Query_Service import AbstractsGetHeightWeightInfoQueryService
from app.infrastructure.db.orm_entity.body_profiles.body_profiles import BodyProfilesORM
from app.infrastructure.db.orm_entity.users.users import UserORM


class GetHeightWeightInfoQueryService(AbstractsGetHeightWeightInfoQueryService):
    def __init__(
        self,
        db_session: Session
    ):
        self.db_session = db_session

    def get_height_weight_info(
            self,
            user_id: UserId,
    ) -> BodyInfo:
        try:
            query =(
                select(
                    BodyProfilesORM.height,
                    BodyProfilesORM.weight_kg,
                    BodyProfilesORM.activity_status
                )
                .where(BodyProfilesORM.user_id == user_id)
                .order_by(BodyProfilesORM.recorded_at.desc())
                .limit(1)
            )
            result = self.db_session.execute(query).first()

            height, weight, activity_status = result

            return BodyInfo(
                height=height,
                weight=weight,
                activity=activity_status
            )
        except:
            raise HTTPException(status_code=404, detail="身体情報を登録してください")
