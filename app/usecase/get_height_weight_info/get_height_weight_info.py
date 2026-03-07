from app.domain.body_info.value_object.get_body_info import BodyInfo
from app.domain.user.value_object.get_user_name import UserId

from app.usecase.get_height_weight_info.height_weight_info_Query_Service import AbstractsGetHeightWeightInfoQueryService


class GetHeightWeightInfoUseCase:
    def __init__(
        self,
        height_weight_info_repository: AbstractsGetHeightWeightInfoQueryService,
    ):
        self.__height_weight_info_repository = height_weight_info_repository
    @property
    def height_weight_info_repository(self) -> AbstractsGetHeightWeightInfoQueryService:
        return self.__height_weight_info_repository

    def get_height_weight_info(
            self,
            user_id: UserId
    ) -> BodyInfo:
        return self.__height_weight_info_repository.get_height_weight_info(user_id)