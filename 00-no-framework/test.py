class HeapsterWatch:
    _hours: int
    _minutes: int

    def __init__(self, hours: int = 0, minutes: int = 0):
        if (hours < 0 or hours > 23):
            raise ValueError(
                'Hours should be in range [0, 23], got %s' % hours)

        if (minutes < 0 or minutes > 59):
            raise ValueError(
                'Minutes should be in range [0, 59], got %s' % minutes)
        self._hours = hours
        self._minutes = minutes

    @property
    def hours(self) -> int:
        return self._hours

    @property
    def minutes(self) -> int:
        return self._minutes

    def to_12_hours(self) -> str:
        pass
        # TODO: implement


# =====
# Tests
# =====

def run_tests():
    pass


if __name__ == '__main__':
    run_tests()
