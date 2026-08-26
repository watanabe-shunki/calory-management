from typing import Annotated

import jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.domain.user.value_object.user_info import Email
from backend.app.infrastructure.security.get_user import UsersQueryService
from backend.app.infrastructure.session import get_db_session
from backend.app.presentation.auth.login import get_settings
from backend.app.usecase.get_user.get_user import GetUserByEmailUseCase
from backend.settings import Settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    settings: Annotated[Settings, Depends(get_settings)],
    db_session: Session = Depends(get_db_session),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        print("token:", token)
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        print("payload:", payload)

        email = payload.get("sub")
        print("email:", email)

        if email is None:
            raise credentials_exception

    except jwt.ExpiredSignatureError as e:
        print("JWT expired:", e)
        raise credentials_exception
    except jwt.InvalidTokenError as e:
        print("JWT invalid:", e)
        raise credentials_exception

    user_by_email_repository = UsersQueryService(db_session)
    usecase = GetUserByEmailUseCase(user_by_email_repository)

    user = usecase.get_user_by_email(Email(email))
    print("user:", user)

    if not user:
        raise credentials_exception

    return user
