import time
from enum import Enum
from typing import List


class UserState(Enum):
    NORMAL = 'NORMAL'
    BANNED = 'BANNED'


class User:
    def __init__(self, username: str, state: UserState):
        self._username: str = username
        self._state: UserState = state

    @property
    def state(self) -> UserState:
        return self._state

    @property
    def username(self) -> str:
        return self._username

    def __eq__(self, other) -> bool:
        if type(other) != type(self):
            return False

        return self.username == other.username


class ForumException(Exception):
    pass


class BannedException(ForumException):
    pass


class AlreadyRegisteredException(ForumException):
    pass


class Forum:
    def __init__(self):
        self._users: List[User] = []

    def is_reachable(self) -> bool:
        # Simulate network latency
        time.sleep(0.01)
        return True

    def register_user(self, user: User):
        if user.state == UserState.BANNED:
            raise BannedException

        if user in self._users:
            raise AlreadyRegisteredException

        self._users.append(user)

    def has_registered_user(self, user: User) -> bool:
        return user in self._users

    def count_users(self) -> int:
        return len(self._users)
