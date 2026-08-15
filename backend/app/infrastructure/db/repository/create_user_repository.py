from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timezone

from backend.app.domain.user.value_object.user_info import Name, Email, UserInfo
from backend.app.usecase.create_user.user_Repository import AbstractCreateUserRepository
from backend.app.infrastructure.db.orm_entity.users.users import UsersORM


class CreateUserRepository(AbstractCreateUserRepository):
    def __init__(
        self,
        db_session: Session,
    ):
        self.db_session = db_session

    def create_user(
        self,
        user_info : UserInfo,
    ) -> None:
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        now = datetime.now(timezone.utc)
        try:
            user = UsersORM(
                email=user_info.email,
                name=user_info.name,
                password_hash=pwd_context.hash(user_info.password),
                auth_provider="password",
                is_active=True,
                created_at=now,
                updated_at=now,
                last_login_at=now,
            )
            self.db_session.add(user)
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()
            raise