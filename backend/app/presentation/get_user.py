from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.query_service.get_user_name import UserNameQueryService
from backend.app.usecase.get_user.get_user import GetUserNameUserCase
from backend.app.domain.user.value_object.get_user_name import UserId
from backend.app.presentation.model.requestbody.get_user.user_id import UserRequestBody
from backend.app.presentation.model.responsebody.get_user.user_name import UserNameResponseBody
router = APIRouter()

@router.post("/{user_id}}", response_model=UserNameResponseBody)
def read_username(
        request: UserRequestBody,
        db_session: Session = Depends(get_db_session)
):
    user_name_repository = UserNameQueryService(db_session)
    use_case = GetUserNameUserCase(user_name_repository)
    user_id = UserId(request.user_id)        # DTO → ドメイン
    username = use_case.get_user_name(user_id)         # UseCase実行
    return UserNameResponseBody(username=str(username))  # ドメイン → DTO
