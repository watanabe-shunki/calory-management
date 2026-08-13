from datetime import timedelta, datetime, timezone
from http.client import HTTPException
from typing import Annotated
import jwt

from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext

from backend.app.domain.user.value_object.user_info import UserEmail
from backend.app.infrastructure.session import get_db_session
from backend.app.infrastructure.security.get_user import UsersQueryService
from backend.app.usecase.get_user.get_user import GetUserByEmailUseCase
from backend.settings import Settings


router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Token(BaseModel):
    access_token: str
    token_type: str

def get_settings():
    return Settings()

def get_user(
    email: UserEmail,
    db_session: Session = Depends(get_db_session)
):
    user_by_email_repository = UsersQueryService(db_session)
    usecase = GetUserByEmailUseCase(user_by_email_repository)
    user = usecase.get_user_by_email(email)
    return user

# plain_passwordがハッシュ化されたパスワードと一致するかを検証する
# passwordが一致する場合は、Trueを返し、そうでない場合は、Falseを返す
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(
    email: UserEmail,
    password: str,
    db_session
):
    user = get_user(email, db_session)
    if not user:
        return False
    if not verify_password(
        password,
        user.password
    ):
        return False
    return user

def create_access_token(
    settings,
    data: dict,
    expires_delta: timedelta | None,
    auth_method="password"
):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire, "auth_method": auth_method})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt

# ログインAPI
@router.post( "/token" )
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    settings: Annotated[Settings, Depends(get_settings)],
    db_session: Session = Depends(get_db_session)
) -> Token:
    # OAuth2PasswordRequestForm では項目名が username だが、
    # このアプリでは username に email を入れて認証する。
    user = authenticate_user(
        UserEmail(form_data.username),
        form_data.password,
        db_session
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    access_token = create_access_token(
        settings,
        data={ "sub" : user.email},
        expires_delta=access_token_expires
    )
    # トークン追加
    return Token(
        access_token=access_token,
        token_type="bearer",
    )
