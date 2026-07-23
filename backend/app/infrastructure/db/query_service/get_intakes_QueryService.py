from datetime import date
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import select

from backend.app.domain.foods_info.value_object.foods_info import (
    FoodsInfo, Calory, Protein
)
from backend.app.domain.user.value_object.get_user_name import UserId
from backend.app.usecase.get_intakes.get_intakes_info_Query_Service import AbstractsGetIntakesInfoQueryService
from backend.app.infrastructure.db.orm_entity.intakes.intakes import IntakeORM


class IntakesQueryService(AbstractsGetIntakesInfoQueryService):
    def __init__(
        self,
        db_session: Session
    ):
        self.db_session = db_session

    def get_intakes_info(
        self,
        user_id: UserId,
    ) -> list[FoodsInfo] | None:
        try:
            query = (
                select(
                    IntakeORM.food_name,
                    IntakeORM.calorie,
                    IntakeORM.protein
                )
                .where(
                    IntakeORM.date == date.today()
                )
            )
            result = self.db_session.execute(query).all()
            # 空でもそのまま返却
            return [
                FoodsInfo(
                    foodsname=intake.food_name,
                    calories=intake.calorie,
                    protein=intake.protein
                )
                for intake in result
            ]

        except SQLAlchemyError:
            raise HTTPException(status_code=500, detail="DBエラー")
