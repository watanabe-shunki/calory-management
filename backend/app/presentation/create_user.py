from fastapi import Depends, APIRouter, status
from sqlalchemy.orm import Session

from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.db.repository.create_user_repository import CreateUserRepository
from backend.app.usecase.create_user.create_user import CreateUser
from backend.app.domain.user.value_object.user_info import UserInfo, Name, Email, Password
from backend.app.presentation.model.requestbody.create_user.request_create_user import UserRequestBody

router = APIRouter()

@router.post(
    "/create_user",
    response_model=None,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    request: UserRequestBody,
    db_session: Session = Depends(get_db_session)
):
    user_repository = CreateUserRepository(db_session=db_session)
    use_case = CreateUser(user_repository)
    user_info = UserInfo(
        name=Name(request.name),
        email=Email(request.email),
        password=Password(request.password),
    )
    return use_case.create_user(user_info)