from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.domain.user.value_object.user_info import UserId
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.query_service.get_height_weight_info_QueryService import HeightWeightInfoQueryService
from backend.app.presentation.auth.security import get_current_user
from backend.app.usecase.get_height_weight_info.get_height_weight_info import GetHeightWeightInfoUseCase
from backend.app.domain.body_info.value_object.get_body_info import (
    HeightCm,
    WeightKg,
    ActivityStatus,
)
from backend.app.presentation.model.requestbody.get_height_weight_info.request_get_height_weight_info import HeightWeightInfoRequest
from backend.app.presentation.model.responsebody.get_height_weight_info.response_get_height_weight_info import BodyInfoResponse
from backend.app.usecase.get_user.user_Query_Service import UserDTO

router = APIRouter()

@router.get(
    "/get_body_info",
    response_model=BodyInfoResponse,
    summary="身体情報を取得するAPI"
)
def get_body_info_by_user_id(
        current_user: Annotated[UserDTO, Depends(get_current_user)],
        session: Session = Depends(get_db_session)
) -> BodyInfoResponse:
    height_weight_info_repository = HeightWeightInfoQueryService(session)
    usecase = GetHeightWeightInfoUseCase(height_weight_info_repository)
    user_id = UserId(current_user.user_id)
    print(user_id)

    result = usecase.get_height_weight_info(user_id)
    print(result)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Body information not found."
        )
    return BodyInfoResponse(
        height=str(result.height), # TODO: ここ強引に型を変えている感じあるので後で調査
        weight=str(result.weight), # TODO: ここ強引に型を変えている感じあるので後で調査
        activity_status=result.activity_status.label,
        activity_status_label=result.activity_status
    )