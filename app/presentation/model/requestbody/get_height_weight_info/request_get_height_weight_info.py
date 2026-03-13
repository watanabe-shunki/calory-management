from pydantic import BaseModel, Field


class HeightWeightInfoRequest(BaseModel):
    user_id: int = Field(
        ..., # "..."←これで必須
        gt=0,
        description="ユーザーID"
    )