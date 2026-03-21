from sqlalchemy.orm import Session

from app.domain.body_info.value_object.get_body_info import BodyInfo

from app.usecase.create_body_info.create_body_info_Repository import AbstractCreateBodyInfoRepository

from app.infrastructure.db.orm_entity.body_profiles.body_profiles import BodyProfilesORM
from app.infrastructure.db.orm_entity.users.users import UsersORM


class CreateBodyInfoRepository(AbstractCreateBodyInfoRepository):
    def __init__(
        self,
        db_session: Session
    ):
        self.db_session = db_session
    def create_body_info(
        self,
        user_id,
        body_info: BodyInfo,
    ) -> None:
        try:
            entity = BodyProfilesORM(
                user_id=user_id,
                height=body_info.height.value,
                weight_kg=body_info.weight.value,
                activity_status=body_info.activity_status
            )
            self.db_session.add(entity)
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()
            raise