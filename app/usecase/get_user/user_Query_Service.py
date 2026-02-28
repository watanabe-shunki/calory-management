from abc import ABC, abstractmethod

from app.domain.user.value_object.get_user_name import UserName, UserId


class AbstractGetUserNameQueryService(ABC):
    @abstractmethod
    def get_user_name(
            self,
            user_id: UserId
    ) -> UserName:
        raise NotImplementedError()
