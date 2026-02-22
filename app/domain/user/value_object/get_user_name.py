class UserId:
    def __init__(self, value: int):
        if value <= 0:
            raise ValueError("invalid get_user id")
        self._value = value

    @property
    def value(self) -> int:
        return self._value


class UserName:
    def __init__(self, value: str):
        if not (1 <= len(value) <= 20):
            raise ValueError("invalid username")
        self._value = value

    def __str__(self) -> str:
        return self._value
