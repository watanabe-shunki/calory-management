from pydantic import BaseModel, Field


class UserNameResponseBody(BaseModel):
    username: str = Field(
        min_length=1,
        max_length=20
    )