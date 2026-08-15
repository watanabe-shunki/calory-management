class UserId:
    def __init__(self, value: int):
        if value <= 0:
            raise ValueError("invalid get_user id")
        self._value = value

    @property
    def value(self) -> int:
        return self._value


class Name:
    def __init__(self, value: str):
        if not (1 <= len(value) <= 20):
            raise ValueError("invalid username")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

class Email:
    def __init__(self, value: str):
        if not (1 <= len(value) <= 30):
            raise ValueError("invalid email")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

class Password:
    def __init__(self, value: str):
        if not (1 <= len(value) <= 72):
            raise ValueError("invalid password")
        self._value = value

    @property
    def value(self) -> str:
        return self._value

class UserInfo:
    def __init__(
        self,
        name: Name,
        email: Email,
        password: Password,
    ):
        self._name = name
        self._email = email
        self._password = password

    @property
    def name(self) -> str:
        return self._name.value

    @property
    def email(self) -> str:
        return self._email.value

    @property
    def password(self) -> str:
        return self._password.value