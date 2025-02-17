from .base import BaseErorr


class UserError(BaseErorr):
    def __str__(self):
        return "User Error"


class UserNotFoundError(UserError):
    def __init__(
        self, *args, user_id: int | None = None, email: str | None = None
    ) -> None:
        super().__init__(*args)
        self._user_id = user_id
        self._email = email

    def __str__(self) -> str:
        if self._user_id is not None and self._email is not None:
            return (
                f"The user was not found."
                f" ID: {self._user_id}, e-mail: {self._email}."
            )
        if self._user_id is not None:
            return f"The user was not found. ID: {self._user_id}."
        if self._email is not None:
            return f"The user with the e-mail {self._email} was not found: e-mail."
        return "The user was not found."
