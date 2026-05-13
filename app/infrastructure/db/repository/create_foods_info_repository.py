from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import select, and_

from app.domain.foods_info.value_object.foods_info import FoodsInfo
from app.infrastructure.db.orm_entity.users.users import UsersORM
from app.infrastructure.db.orm_entity.daily_records.deily_records import DailyRecordsORM
from app.infrastructure.db.orm_entity.intakes.intakes import IntakeORM
from app.usecase.create_foods_info.create_foods_info_Repository import AbstractCreateFoodsInfoRepository
from app.usecase.create_foods_info.create_foods_info import CreateFoodsInfo


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
            daily = self.get_daily_records(
                user_id,
                foods_info.meal_date
            )
            if not daily:
                daily = DailyRecordsORM(
                    user_id=user_id,
                    date=date.today(),
                )
                self.db_session.add(daily)
                self.db_session.flush()

            intake_entity = IntakeORM(
                daily_unit_id=daily.id,
                food_name=foods_info.foods_name.foodsname,
                calorie=foods_info.calories.calories,
                protein=foods_info.protein.protein
            )
            self.db_session.add(intake_entity)
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()
            raise

    def get_daily_records(
        self,
        user_id,
        meal_date
    ):
        try:
            daily = self.db_session.execute(select(
                DailyRecordsORM
            ).where(
                and_(
                    DailyRecordsORM.date == meal_date,
                    DailyRecordsORM.user_id == user_id
                )
            )).scalar_one_or_none()
            return daily
        except Exception:
            self.db_session.rollback()