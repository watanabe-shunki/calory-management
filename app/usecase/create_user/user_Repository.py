from abc import ABC, abstractmethod

from app.domain.user.value_object.get_user_name import UserName

class AbstractCreateUserRepository(ABC):
    @abstractmethod
    def create_user(
            self,
            name: UserName
    ):
        raise NotImplementedError