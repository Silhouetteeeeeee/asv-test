import time

class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(100000):
            self.d[x] = None

    def time_keys(self):
        time.sleep(1)
        for key in self.d.keys():
            pass

    def time_iterkeys(self):
        time.sleep(1)
        for key in self.d.iterkeys():
            pass

    def time_range(self):
        time.sleep(1)
        d = self.d
        for key in range(100000):
            x = d[key]

    def time_xrange(self):
        time.sleep(1)
        d = self.d
        for key in range(100000):
            x = d[key]


class MemSuite:
    def mem_list(self):
        return [0] * 256