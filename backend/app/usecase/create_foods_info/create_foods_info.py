from backend.app.usecase.create_foods_info.create_foods_info_Repository import AbstractCreateFoodsInfoRepository
from backend.app.domain.foods_info.value_object.foods_info import FoodsInfo

class CreateFoodsInfo:
    def __init__(
        self,
        create_foods_info_repository: AbstractCreateFoodsInfoRepository
    ):
        self.__create_foods_info_repository = create_foods_info_repository

    def create_foods_info(
        self,
        user_id,
        foods_info: FoodsInfo
    ):
        # TODO:後でユーザーIDも登録データに入れる必要がある
        self.__create_foods_info_repository.create_foods_info(
            user_id,
            foods_info
        )