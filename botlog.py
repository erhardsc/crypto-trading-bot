from __future__ import print_function
from config import CONFIG
import sys
from pyspin.spin import Default, Spinner


class BotLog(object):
    def __init__(self):
        self.spin = Spinner(Default)

    def log(self, message):
        if (CONFIG['VERBOSE']):
            print(message)
        else:
            print(u"\r{0}".format(self.spin.next()), end="")
            sys.stdout.flush()
