from botlog import BotLog
import sys
import getopt
import time


class BotCandlestick(object):
    def __init__(self,
                 period=300,
                 date=0,
                 open=0,
                 close=0,
                 high=0,
                 low=0,
                 priceAverage=0):
        self.date = date
        self.current = 0
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.startTime = time.time()
        self.period = period
        self.output = BotLog()
        self.priceAverage = priceAverage
        self.graph_data = []

    def tick(self, price):
        self.current = float(price)
        if (self.open is None):
            self.open = self.current

        if ((self.high is None) or (self.current > self.high)):
            self.high = self.current

        if ((self.low is None) or (self.current < self.low)):
            self.low = self.current

        if (time.time() >= (self.startTime + self.period)):
            self.close = self.current
            self.priceAverage = (self.high + self.low + self.close) / float(3)

        self.output.log("Open: " + str(self.open) + " Close: " + str(
            self.close) + " High: " + str(self.high) + " Low: " +
                        str(self.low) + " Current: " + str(self.current))

    def isClosed(self):
        if (self.close is not None):
            return True
        else:
            return False
