from datetime import date
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.domain.foods_info.value_object.foods_info import (
    FoodsInfo, MealDate,FoodsName, Calory, Protein
)
from app.infrastructure.session import get_db_session
from app.infrastructure.db.repository.create_foods_info_repository import CreateFoodsInfoRepository
from app.usecase.create_foods_info.create_foods_info import CreateFoodsInfo
from app.presentation.model.requestbody.create_foods_info.create_foods_info_DTO import CreateFoodsInfoDTO


router = APIRouter()

@router.post(
    "/create_foods_info",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="日単位の食事の情報を登録するAPI"
)
def create_foods_info(
    request: CreateFoodsInfoDTO,
    db_session: Session = Depends(get_db_session)
):
    user_id = 1
    foods_repository = CreateFoodsInfoRepository(db_session=db_session)
    usecase = CreateFoodsInfo(foods_repository)

    foods_info = FoodsInfo(
        mealdate=MealDate(date.today()),
        foodsname=FoodsName(request.foods_name),
        calories=Calory(request.calory),
        protein=Protein(request.protein),
    )

    return usecase.create_foods_info(user_id, foods_info)
