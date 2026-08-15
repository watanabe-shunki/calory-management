from abc import ABC, abstractmethod

from backend.app.domain.user.value_object.user_info import Name, UserId, Email, Password
from dataclasses import dataclass


@dataclass
class UserDTO:
     email: str
     password: str
     is_active: bool


class AbstractGetUserNameQueryService(ABC):
    @abstractmethod
    def get_user_name(
            self,
            email: Email
    ) -> Name:
        raise NotImplementedError()

class AbstractGetUserByEmailQueryService(ABC):
    @abstractmethod
    def get_user_by_email(
        self,
        email: Email
    ) -> UserDTO:
        raise NotImplementedError()