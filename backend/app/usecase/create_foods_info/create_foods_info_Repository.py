from abc import ABC, abstractmethod
from backend.app.domain.foods_info.value_object.foods_info import FoodsInfo
from backend.app.domain.user.value_object.user_info import UserId


class AbstractCreateFoodsInfoRepository(ABC):
    @abstractmethod
    def create_foods_info(
        self,
        user_id: UserId,
        foods_info: FoodsInfo
    ):
        return NotImplemented