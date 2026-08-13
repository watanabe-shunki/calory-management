from sqlalchemy.orm import Session

from backend.app.domain.user.value_object.user_info import UserName
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
        username: UserName,
    ) -> None:
        try:
            user = UsersORM(user_id=user_id)
            self.db_session.add(user)
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()
            raise