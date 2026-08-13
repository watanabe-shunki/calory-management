from abc import ABC

from backend.app.domain.user.value_object.user_info import UserName, UserId, UserEmail
from backend.app.infrastructure.security.get_user import UserDTO
from backend.app.usecase.get_user.user_Query_Service import AbstractGetUserNameQueryService, \
    AbstractGetUserByEmailQueryService


class GetUserNameUserCase:
    def __init__(
        self,
        user_name_repository: AbstractGetUserNameQueryService
    ):
        self.__user_name_repository = user_name_repository
    @property
    def user_name_repository(self) -> AbstractGetUserNameQueryService:
        return self.__user_name_repository

    def get_user_name(
            self,
            user_id: UserId
    ) -> UserName:
        return self.__user_name_repository.get_user_name(user_id)


class GetUserByEmailUseCase:
    def __init__(
            self,
            user_by_email_repository: AbstractGetUserByEmailQueryService
    ):
        self.__user_by_email_repository = user_by_email_repository
    @property
    def user_by_email_repository(self) -> AbstractGetUserByEmailQueryService:
        return self.__user_by_email_repository

    def get_user_by_email(
            self,
            email: UserEmail
    ) -> UserDTO:
        return self.__user_by_email_repository.get_user_by_email(email)
