from abc import ABC, abstractmethod
from app.domain.foods_info.value_object.foods_info import FoodsInfo

class AbstractCreateFoodsInfoRepository(ABC):
    @abstractmethod
    def create_foods_info(
        self,
        user_id,
        foods_info: FoodsInfo
    ):
        return NotImplemented