from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.domain.user.value_object.get_user_name import UserId
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.query_service.get_height_weight_info_QueryService import HeightWeightInfoQueryService
from backend.app.usecase.get_height_weight_info.get_height_weight_info import GetHeightWeightInfoUseCase
from backend.app.domain.body_info.value_object.get_body_info import (
    HeightCm,
    WeightKg,
    ActivityStatus,
)
from backend.app.presentation.model.requestbody.get_height_weight_info.request_get_height_weight_info import HeightWeightInfoRequest
from backend.app.presentation.model.responsebody.get_height_weight_info.response_get_height_weight_info import BodyInfoResponse
router = APIRouter()

@router.get(
    "/get_body_info/{user_id}",
    response_model=BodyInfoResponse,
    summary="身体情報を取得するAPI"
)
def get_body_info_by_user_id(
        user_id: int,
        session: Session = Depends(get_db_session)
) -> BodyInfoResponse:
    height_weight_info_repository = HeightWeightInfoQueryService(session)
    usecase = GetHeightWeightInfoUseCase(height_weight_info_repository)
    user_id = UserId(user_id)
    result = usecase.get_height_weight_info(user_id)
    return BodyInfoResponse(
        height=str(result.height), # TODO: ここ強引に型を変えている感じあるので後で調査
        weight=str(result.weight), # TODO: ここ強引に型を変えている感じあるので後で調査
        activity_status=result.activity_status.label,
        activity_status_label=result.activity_status
    )