import unittest


class HeapsterWatch:
    def __init__(self, hours: int = 0, minutes: int = 0):
        if (hours < 0 or hours > 23):
            raise ValueError(
                'Hours should be in range [0, 23], got %s' % hours)

        if (minutes < 0 or minutes > 59):
            raise ValueError(
                'Minutes should be in range [0, 59], got %s' % minutes)
        # self._hours = hours
        # self._minutes = minutes

        self._minutes = 60 * hours + minutes

    def _normalize(self):
        self._minutes %= 1440
        # self._hours %= 23
        # self._minutes %= 59

    def display(self) -> str:
        hours = (self._minutes // 60) % 24
        minutes = (self._minutes % 60)
        # hours = self._hours
        # minutes = self._minutes
        return "%02d:%02d" % (hours, minutes)

    def inc_hours(self):
        self._minutes += 60
        # self._hours += 1
        self._normalize()

    def dec_hours(self):
        self._minutes -= 60
        # self._hours -= 1
        self._normalize()

    def inc_minutes(self):
        self._minutes += 1
        # if self._minutes > 59:
        #     self._hours += 1
        self._normalize()

    def dec_minutes(self):
        self._minutes -= 1
        # if self._minutes < 0:
        #     self._hours -= 1
        self._normalize()


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
        self.assertEqual(watch._minutes, 673)
