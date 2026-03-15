from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from starlette import status

from app.domain.body_info.value_object.get_body_info import (
    BodyInfo,
    HeightCm,
    WeightKg
)
from app.infrastructure.session import get_db_session
from app.infrastructure.db.repository.create_body_info_repository import CreateBodyInfoRepository
from app.usecase.create_body_info.create_body_info import CreateBodyInfo
from app.presentation.model.requestbody.create_body_info.request_create_body_info import BodyInfosRequestBody

router = APIRouter()

@router.post(
    "/create_body_info",
    response_model=None,
    status_code=status.HTTP_201_CREATED
)
def create_body_info(
        request: BodyInfosRequestBody,
        db_session: Session = Depends(get_db_session)
):
    user_id = 1
    body_info_repository = CreateBodyInfoRepository(db_session=db_session)
    usecase = CreateBodyInfo(body_info_repository)
    body_info = BodyInfo(
        height=HeightCm(request.height),
        weight=WeightKg(request.weight),
        activity_status=request.activity_status,
    )
    return  usecase.create_body_info(user_id, body_info)