from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import select, and_

from backend.app.domain.foods_info.value_object.foods_info import FoodsInfo
from backend.app.infrastructure.db.orm_entity.intakes.intakes import IntakeORM
from backend.app.usecase.create_foods_info.create_foods_info_Repository import AbstractCreateFoodsInfoRepository


class CreateFoodsInfoRepository(AbstractCreateFoodsInfoRepository):
    def __init__(
        self,
        db_session: Session
    ):
        self.db_session = db_session
    def create_foods_info(
        self,
        user_id,
        foods_info: FoodsInfo
    ):
        try:
            intake_entity = IntakeORM(
                user_id=user_id,
                food_name=foods_info.foods_name.foodsname,
                calorie=foods_info.calories.calories,
                protein=foods_info.protein.protein,
                date=date.today()
            )
            self.db_session.add(intake_entity)
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()
            raise
