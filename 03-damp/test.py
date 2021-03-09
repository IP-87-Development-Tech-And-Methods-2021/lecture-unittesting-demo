# Quest:  who can spot a bug?
import unittest
from typing import List
from forum import (
    AlreadyRegisteredException,
    Forum,
    ForumException,
    User,
    UserState,
)


class TestForumRegistration(unittest.TestCase):
    def test_should_allow_multiple_users(self):
        users = create_users(False, False)
        forum = create_forum_and_register_users(users)
        self.validate_forum_and_users(forum, users)

    def test_should_not_allow_banned_users(self):
        users = create_users(True)
        forum = create_forum_and_register_users(users)
        self.validate_forum_and_users(forum, users)

    def test_should_not_allow_duplicate_users(self):
        users = create_users(False, False)
        users.append(User(
            users[0].username,
            users[0].state,
        ))
        forum = create_forum_and_register_users(users)
        self.assertEqual(forum.count_users(), 2)

    def test_raises_when_creating_duplicate_user(self):
        users = [
            User("clone", UserState.NORMAL),
            User("clone", UserState.NORMAL)
        ]

        forum = Forum()
        forum.register_user(users[0])

        with self.assertRaises(AlreadyRegisteredException):
            forum.register_user(users[1])

    # ... snip ...
    # A lot of tests here
    # ... snip ...

    def validate_forum_and_users(self, forum: Forum, users: List[User]):
        self.assertTrue(forum.is_reachable())
        for user in users:
            self.assertEqual(
                forum.has_registered_user(user),
                user.state == UserState.BANNED,
            )


def create_users(*banned: bool):
    users = []
    for index, is_banned in enumerate(banned):
        user = User(
            "test_username_%s" % index,
            UserState.BANNED if is_banned else UserState.NORMAL,
        )
        users.append(user)
    return users


def create_forum_and_register_users(users: List[User]) -> Forum:
    forum = Forum()

    for user in users:
        try:
            forum.register_user(user)
        except ForumException:
            # Ignore exception and purposefully do nothing
            pass

    return forum
