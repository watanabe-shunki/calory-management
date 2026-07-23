from backend.app.domain.user.value_object.get_user_name import UserId
from backend.app.domain.foods_info.value_object.foods_info import FoodsInfo

from backend.app.usecase.get_intakes.get_intakes_info_Query_Service import AbstractsGetIntakesInfoQueryService


class GetIntakesInfoUseCase:
    def __init__(
        self,
        get_intakes_info_query_service: AbstractsGetIntakesInfoQueryService
    ):
        self.__get_intakes_info_query_service = get_intakes_info_query_service

    @property
    def get_intakes_info_query_service(self) -> AbstractsGetIntakesInfoQueryService:
        return self.__get_intakes_info_query_service

    def get_intakes_info(
        self,
        user_id: UserId
    ) -> list[FoodsInfo] | None:
        return self.__get_intakes_info_query_service.get_intakes_info(user_id)