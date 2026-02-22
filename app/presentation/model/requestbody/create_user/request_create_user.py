from pydantic import BaseModel, Field


class UserRequestBody(BaseModel):
    username: str = Field(
        max_length=30
    )