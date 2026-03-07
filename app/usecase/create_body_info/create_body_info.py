from abc import ABC, abstractmethod

from app.domain.body_info.value_object.get_body_info import BodyInfo

class AbstractCreateBodyInfo(ABC):
    @abstractmethod
    def create_body_info(
            self,
            body_info: BodyInfo
    ):
        raise NotImplementedError # TODO: なんとなく使っていたので実際にどういう動きをしているか確認する