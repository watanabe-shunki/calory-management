from pydantic import BaseModel, Field


class IntakesInfoResponse(BaseModel):
    food_name: str = Field(
        ...,
        description="FoodsName"
    )
    calory: str = Field(
        max_length=4,
        description="calory"
    )
    protein: str = Field(
        max_length=3,
        description="protein"
    )