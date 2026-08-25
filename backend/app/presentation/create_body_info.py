from typing import Annotated

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from backend.app.domain.user.value_object.user_info import UserId
from backend.app.domain.body_info.value_object.get_body_info import (
    BodyInfo,
    HeightCm,
    WeightKg
)
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.repository.create_body_info_repository import CreateBodyInfoRepository
from backend.app.presentation.auth.security import get_current_user
from backend.app.usecase.create_body_info.create_body_info import CreateBodyInfo
from backend.app.usecase.get_user.user_Query_Service import UserDTO
from backend.app.presentation.model.requestbody.create_body_info.request_create_body_info import BodyInfosRequestBody

router = APIRouter()

@router.post(
    "/create_body_info",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
    summary="身体情報を登録するAPI"
)
def create_body_info(
    request: BodyInfosRequestBody,
    current_user: Annotated[UserDTO, Depends(get_current_user)],
    db_session: Session = Depends(get_db_session)
):
    user_id = UserId(current_user.user_id)
    if user_id.value != current_user.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This is not a registered account. No user information is available.",
        )
    body_info_repository = CreateBodyInfoRepository(db_session=db_session)
    usecase = CreateBodyInfo(body_info_repository)
    body_info = BodyInfo(
        height=HeightCm(request.height),
        weight=WeightKg(request.weight),
        activity_status=request.activity_status,
    )
    return  usecase.create_body_info(user_id, body_info)