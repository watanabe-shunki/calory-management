from pydantic import BaseModel, Field
from app.domain.body_info.enums.activity_level import ActivityStatus


class BodyInfosRequestBody(BaseModel):
    height: str = Field(
        max_length=3,
        description="身長"
    )
    weight: str = Field(
        max_length=3,
        description="体重"
    )
    activity_status: ActivityStatus = Field(
        ...,
        description="生活レベルステータス"
    )
