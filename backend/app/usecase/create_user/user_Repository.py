from abc import ABC, abstractmethod

from backend.app.domain.user.value_object.user_info import Name, UserInfo


class AbstractCreateUserRepository(ABC):
    @abstractmethod
    def create_user(
            self,
            user_info: UserInfo
    ):
        raise NotImplementedError