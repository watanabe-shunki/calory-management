from pydantic import BaseModel, Field


class UserRequestBody(BaseModel):
    name: str = Field(
        max_length=30
    )
    email: str = Field(
        max_length=30
    )
    password: str = Field(
        min_length=8,
        max_length=72,
    )