from pydantic import BaseModel
from datetime import date


class CreateFoodsInfoDTO(BaseModel):
    foods_name: str
    calory: int
    protein: float
