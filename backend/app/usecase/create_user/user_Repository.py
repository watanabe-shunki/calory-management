from abc import ABC, abstractmethod

from backend.app.domain.user.value_object.user_info import UserName

class AbstractCreateUserRepository(ABC):
    @abstractmethod
    def create_user(
            self,
            name: UserName
    ):
        raise NotImplementedError