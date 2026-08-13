from backend.app.usecase.create_user.user_Repository import AbstractCreateUserRepository

from backend.app.domain.user.value_object.user_info import UserName

class CreateUser:
    def __init__(
        self,
        user_name_repository: AbstractCreateUserRepository
    ):
        self.__user_name_repository = user_name_repository
    @property
    def user_name_repository(self) -> AbstractCreateUserRepository:
        return self.__user_name_repository

    def create_user(
            self,
            user_name: UserName
    ) -> None:
        self.__user_name_repository.create_user(user_name)