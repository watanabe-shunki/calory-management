from datetime import date
from app.domain.body_info.enums.activity_level import ActivityStatus

"""
以下のエンティティはここでは不要
- ActivityLevel: Enumで定義しているため
- RecordedAt: DB側で日付を作成(Create)しているため
"""
class HeightCm:
    def __init__(self, value: str):
        if value is None:
            raise ValueError("invalid height value")
        if not (100 <= int(value) <= 230):
            raise ValueError("height out of range")
        self._value = value

class WeightKg:
    def __init__(self, value: str):
        if value is None:
            raise ValueError("invalid weight value")
        if not (30 <= int(value) <= 300):
            raise ValueError("weight out of range")
        self._value = value

class BodyInfo:
    def __init__(
        self,
        height: HeightCm,
        weight: WeightKg,
        activity: ActivityStatus,
    ):
        self.height = height
        self.weight = weight
        self.activity = activity