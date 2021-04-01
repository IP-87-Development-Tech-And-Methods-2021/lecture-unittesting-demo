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
        am_pm = 'AM'
        hours = self._hours
        minutes = self._minutes

        if hours >= 12:
            am_pm = 'PM'

        if hours == 0:
            hours = 24

        if hours > 12:
            hours -= 12

        return '%02d:%02d %2s' % (hours, minutes, am_pm)


# =====
# Tests
# =====

def run_tests():
    watch = HeapsterWatch(0, 0)
    print(watch.to_12_hours())  # should be 12:00 AM

    watch = HeapsterWatch(11, 43)
    print(watch.to_12_hours())  # should be 11:43 AM

    watch = HeapsterWatch(12, 0)
    print(watch.to_12_hours())  # should be 12:00 PM

    watch = HeapsterWatch(23, 43)
    print(watch.to_12_hours())  # should be 11:43 PM


if __name__ == '__main__':
    run_tests()
