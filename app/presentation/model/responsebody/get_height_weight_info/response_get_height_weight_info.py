from pydantic import BaseModel, Field


class BodyInfoResponse(BaseModel):
    height: str = Field(
        min_length=3,
        max_length=3
    )
    weight: str = Field(
        min_length=2,
        max_length=3
    )
    activity_status: str = Field(
        ...,
        description="生活レベルステータス"
    )
    activity_status_label: str = Field(
        ...,
        description="生活レベルのラベル: 実際の文字列"
    )