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

    @property
    def hours(self) -> int:
        return self._hours

    @property
    def minutes(self) -> int:
        return self._minutes

    def display(self) -> str:
        return "%02d:%02d" % (self._hours, self._minutes)

    def inc_hours(self):
        self._hours += 1

    def dec_hours(self):
        self._hours -= 1

    def inc_minutes(self):
        self._minutes += 1

    def dec_minutes(self):
        self._minutes -= 1


# =====
# Tests
# =====

class TestHeapsterWatch(unittest.TestCase):

    # The following test breaks AAA rule
    def test_all_in_one(self):
        watch = HeapsterWatch(0, 13)

        self.assertEquals(watch.display(), "00:13")

        watch.dec_hours()

        self.assertEquals(watch.display(), "23:13")

        watch.dec_minutes()

        self.assertEquals(watch.display(), "23:12")

        watch.inc_hours()

        self.assertEquals(watch.display(), "00:12")

        watch.inc_minutes()

        self.assertEquals(watch.display(), "00:13")

        watch = HeapsterWatch(23, 59)

        watch.inc_minutes()

        self.assertEquals(watch.display(), "00:00")

        watch.dec_minutes()

        self.assertEquals(watch.display(), "23:59")
