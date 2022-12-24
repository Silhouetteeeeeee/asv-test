import time

def f(x):
    for i in range(x):
        for j in range(x):
            print(" ")

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        f(100)

    def time_keys(self):
        f(100)

    def time_iterkeys(self):
        f(100)

    def time_range(self):
        f(100)

    def time_xrange(self):
        f(100)


class MemSuite:
    def mem_list(self):
        return [0] * 256