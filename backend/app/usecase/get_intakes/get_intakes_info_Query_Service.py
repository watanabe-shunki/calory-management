from abc import ABC, abstractmethod

from backend.app.domain.user.value_object.user_info import UserId
from backend.app.domain.foods_info.value_object.foods_info import FoodsInfo


class AbstractsGetIntakesInfoQueryService(ABC):
    @abstractmethod
    def get_intakes_info(
        self,
        user_id: UserId
    ) -> list[FoodsInfo] | None:
        raise NotImplementedError()