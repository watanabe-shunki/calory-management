from abc import ABC, abstractmethod

from backend.app.domain.user.value_object.user_info import UserName, UserId, UserEmail
from backend.app.infrastructure.security.get_user import UserDTO


class AbstractGetUserNameQueryService(ABC):
    @abstractmethod
    def get_user_name(
            self,
            user_id: UserId
    ) -> UserName:
        raise NotImplementedError()

class AbstractGetUserByEmailQueryService(ABC):
    @abstractmethod
    def get_user_by_email(
        self,
        email: UserEmail
    ) -> UserDTO:
        raise NotImplementedError()