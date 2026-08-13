from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.domain.user.value_object.user_info import UserId
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.query_service.get_intakes_QueryService import IntakesQueryService
from backend.app.usecase.get_intakes.get_intakes_info import GetIntakesInfoUseCase
from backend.app.presentation.model.responsebody.get_intakes_info.response_get_intakes_info import IntakesInfoResponse


router = APIRouter()


@router.get(
    "/get_intakes_info/{user_id}",
    response_model=list[IntakesInfoResponse],
    summary="食事情報を取得するAPI"
)
def get_intakes_info(
    user_id: int,
    session: Session = Depends(get_db_session)
) -> list[IntakesInfoResponse] | None:
    intakes_info_repository = IntakesQueryService(session)
    usecase = GetIntakesInfoUseCase(intakes_info_repository)
    user_id = UserId(user_id)
    result = usecase.get_intakes_info(user_id=user_id)

    if result is None:
        return None
    return [
        IntakesInfoResponse(
            food_name=row.foods_name,
            calory=row.calories,
            protein=row.protein
        )
        for row in result
    ]