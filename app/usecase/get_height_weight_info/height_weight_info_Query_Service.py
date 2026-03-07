from abc import ABC, abstractmethod

from app.domain.body_info.value_object.get_body_info import BodyInfo
from app.domain.user.value_object.get_user_name import UserId

class AbstractsGetHeightWeightInfoQueryService(ABC):
    @abstractmethod
    def get_height_weight_info(
            self,
            user_id: UserId,
    ) -> BodyInfo:
        raise NotImplementedError()
