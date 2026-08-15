from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select

from backend.app.infrastructure.db.orm_entity.users.users import UsersORM
from backend.app.domain.user.value_object.user_info import Email
from backend.app.usecase.get_user.user_Query_Service import AbstractGetUserByEmailQueryService, UserDTO


class UsersQueryService(AbstractGetUserByEmailQueryService):
     def __init__(
         self,
         db_session: Session
     ):
         self.db_session = db_session

     def get_user_by_email(
          self,
          email: Email
     ) -> UserDTO:
          try:
               query = (
                    select(UsersORM)
                    .select_from(UsersORM)
                    .where(UsersORM.email == email.value)
               )
               result = self.db_session.execute(query).scalar()
               return UserDTO(result.email, result.password_hash, result.is_active)
          except:
               raise HTTPException(status_code=404, detail="Email does not exist")
