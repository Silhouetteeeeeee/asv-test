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
        for key in self.d.keys():
            pass

    def time_iterkeys(self):
        for key in self.d.iterkeys():
            pass

    def time_range(self):
        d = self.d
        for key in range(100000):
            x = d[key]

    def time_xrange(self):
        d = self.d
        for key in range(100000):
            x = d[key]


class MemSuite:
    def mem_list(self):
        return [0] * 256