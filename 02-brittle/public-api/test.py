import unittest


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

        # self._minutes = 60 * hours + minutes

    def display(self) -> str:
        # hours = (self.minutes // 60) % 24
        # minutes = (self.minutes % 60)
        hours = self._hours
        minutes = self._minutes
        return "%02d:%02d" % (hours, minutes)

    def inc_hours(self):
        # self._minutes += 60
        self._hours += 1

    def dec_hours(self):
        # self._minutes -= 60
        self._hours -= 1

    def inc_minutes(self):
        self._minutes += 1

    def dec_minutes(self):
        self._minutes -= 1


# =====
# Tests
# =====

class TestHeapsterWatch(unittest.TestCase):

    # The following test will fail as soon as internal implementation
    # of HeapsterWatch will change
    def test_increase_hours(self):
        # Arrange
        watch = HeapsterWatch(10, 13)

        # Act
        watch.inc_hours()

        # Assert
        self.assertEqual(watch._hours, 11)
