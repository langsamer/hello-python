import time

import gevent
import math


def timed_sequence(interval=0.5):
    def generator():
        while True:
            value = time.clock()
            yield math.sin(value)
            gevent.sleep(interval)
    return generator()