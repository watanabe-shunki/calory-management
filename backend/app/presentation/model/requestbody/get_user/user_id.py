from pydantic import BaseModel, Field


class UserRequestBody(BaseModel):
    user_id: int = Field(
        ge=1 # 1以上の値が必要という制約
    )
