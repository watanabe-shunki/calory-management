from abc import ABC, abstractmethod

from backend.app.domain.user.value_object.user_info import UserName, UserId, UserEmail, UserPassword
from dataclasses import dataclass


@dataclass
class UserDTO:
     email: UserEmail
     password: UserPassword
     is_active: bool


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