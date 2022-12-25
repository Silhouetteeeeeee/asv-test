import time
import sys
import os
sys.path.append("D:\项目\项目2022-12\ASV-case\benchmarks")
import mypackage.cal as cal
class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None
        time.sleep(1)

    def time_keys(self):
        cal.f(100)

    def time_iterkeys(self):
        for key in self.d.iterkeys():
            pass

    def time_range(self):
        d = self.d
        for key in range(500):
            x = d[key]

    def time_xrange(self):
        d = self.d
        for key in range(500):
            x = d[key]


class MemSuite:
    def mem_list(self):
        return [0] * 256