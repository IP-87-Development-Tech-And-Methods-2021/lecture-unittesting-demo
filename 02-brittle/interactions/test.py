import unittest

from datetime import datetime
from typing import Optional
from unittest import mock

from storage import Storage


class RegistrationSystem:
    def __init__(self):
        self.storage = Storage()

    def create_account(self, username: str):
        account = {"username": username, "created_at": datetime.now()}
        self.storage.put(account)

    def retrieve_account(self, username: str) -> Optional[dict]:
        accounts = self.storage.list_all()
        for account in accounts:
            if account.username == username:
                return account
        return None


# =====
# Tests
# =====

class TestRegistrationSystem(unittest.TestCase):

    # What if due to underlying bug we did not save accout?
    @mock.patch('storage.Storage.put')
    def test_creates_user(self, storage_put):
        system = RegistrationSystem()

        system.create_account("foobar")

        storage_put.assert_called_once()

    # What if internal implementation changes?
    @mock.patch('storage.Storage.list_all')
    def test_retrieves_nonexisting_user(self, storage_list):
        system = RegistrationSystem()

        account = system.retrieve_account("non-existing")

        storage_list.assert_called_once()
        self.assertIsNone(account)
