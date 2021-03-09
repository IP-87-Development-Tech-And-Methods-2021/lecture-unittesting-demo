from typing import List, Optional


class Storage:

    def __init__(self):
        self._kv = {}

    def put(self, account: dict):
        # if account.username not in self._kv:
        #     self._kv[account.username] = account
        pass

    def find_by_username(self, username: str) -> Optional[dict]:
        return self._kv.get(username)

    def list_all(self) -> List[dict]:
        return list(self._kv.values())
