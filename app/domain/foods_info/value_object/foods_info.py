from datetime import date

from sqlalchemy import MetaData

from app.infrastructure.db.orm_entity.types import metadata


# 日時
# class MealDate:
#     def __init__(self, foodsdate: date):
#         if foodsdate > date.today():
#             raise ValueError("date cannot be in the future")
#
#         self._foodsdate = foodsdate
#
#     @property
#     def  foodsdate(self) -> date:
#         return self._foodsdate

# 食事名
class FoodsName:
    def __init__(self, foodsname: str):
        if len(foodsname) > 20:
            raise ValueError("foodsname cannot be greater than 20")

        self._foodsname = foodsname

    @property
    def foodsname(self) -> str:
        return self._foodsname

# カロリー
class Calory:
    def __init__(self, calories: int):
        if calories < 0:
            raise ValueError("calories cannot be negative")
        if calories > 9999:
            raise ValueError("calories cannot be greater than 9999")

        self._calories = calories

    @property
    def calories(self) -> int:
        return self._calories

# タンパク質
class Protein:
    def __init__(self, protein: float):
        if protein > 300:
            raise ValueError("protein is unrealistic")

        self._protein = protein

    @property
    def protein(self):
        return self._protein

class FoodsInfo:
    def __init__(
        self,
        # mealdate: MealDate,
        foodsname: FoodsName,
        calories: Calory,
        protein: Protein,
    ):
        # self._mealdate = mealdate
        self._foodsname = foodsname
        self._calories = calories
        self._protein = protein

    # @property
    # def meal_date(self):
    #     return self._mealdate

    @property
    def foods_name(self):
        return self._foodsname

    @property
    def calories(self):
        return self._calories

    @property
    def protein(self):
        return self._protein
