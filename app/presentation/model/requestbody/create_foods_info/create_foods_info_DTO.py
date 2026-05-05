from pydantic import BaseModel
from datetime import date


class CreateFoodsInfoDTO(BaseModel):
    date: date
    foods_name: str
    calory: int
    protein: float
