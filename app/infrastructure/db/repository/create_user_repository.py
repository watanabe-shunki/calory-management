from sqlalchemy.orm import Session
from streamlit import rerun

from app.domain.user.value_object.get_user_name import UserName
from app.usecase.create_user.user_Repository import AbstractCreateUserRepository
from app.infrastructure.db.orm_entity.user.user import UserORM


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
            user = UserORM(name=username)
            self.db_session.add(user)
            self.db_session.commit()
        except Exception:
            self.db_session.rollback()
            raise