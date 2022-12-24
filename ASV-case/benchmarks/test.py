import time
import calculate1

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        calculate1.f(100)

    def time_keys(self):
        calculate1.f(1000)

    def time_iterkeys(self):
        calculate1.f(10000)

    def time_range(self):
        calculate1.f(100000)

    def time_xrange(self):
        calculate1.f(1000000)


class MemSuite:
    def mem_list(self):
        return [0] * 256