from app.domain.body_info.value_object.get_body_info import BodyInfo

from app.usecase.create_body_info.create_body_info_Repository import AbstractCreateBodyInfoRepository


class CreateBodyInfo:
    def __init__(
            self,
        body_info_repository: AbstractCreateBodyInfoRepository
    ):
        self.__body_info_repository = body_info_repository

    def create_body_info(
            self,
            user_id,
            body_info: BodyInfo
    ) -> None:
        self.__body_info_repository.create_body_info(
            user_id,
            body_info
        )



