from app.domain.user.value_object.get_user_name import UserName, UserId
from app.usecase.get_user.user_Query_Service import AbstractGetUserNameQueryService

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
