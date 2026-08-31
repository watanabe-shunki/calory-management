from typing import Annotated

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from backend.app.domain.foods_info.value_object.foods_info import (
    FoodsInfo, FoodsName, Calory, Protein
)
from backend.app.domain.user.value_object.user_info import UserId
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.repository.create_foods_info_repository import CreateFoodsInfoRepository
from backend.app.presentation.auth.security import get_current_user
from backend.app.usecase.create_foods_info.create_foods_info import CreateFoodsInfo
from backend.app.presentation.model.requestbody.create_foods_info.create_foods_info_DTO import CreateFoodsInfoDTO
from backend.app.usecase.get_user.user_Query_Service import UserDTO

router = APIRouter()

@router.post(
    "/create_foods_info",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="日単位の食事の情報を登録するAPI"
)
def create_foods_info(
    request: CreateFoodsInfoDTO,
    current_user: Annotated[UserDTO, Depends(get_current_user)],
    db_session: Session = Depends(get_db_session)
):
    user_id = UserId(current_user.user_id)
    foods_repository = CreateFoodsInfoRepository(db_session=db_session)
    usecase = CreateFoodsInfo(foods_repository)

    foods_info = FoodsInfo(
        foodsname=FoodsName(request.foods_name),
        calories=Calory(request.calory),
        protein=Protein(request.protein),
    )

    return usecase.create_foods_info(user_id, foods_info)
