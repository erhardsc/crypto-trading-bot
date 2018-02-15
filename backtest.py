import sys
import getopt

from botchart import BotChart
from botstrategy import BotStrategy


# Testing historical price data.
def main(argv):
    startTime = 1504224000
    endTime = 1506815999
    chart = BotChart(startTime, endTime, "poloniex", "BTS/BTC", "1d")
    strategy = BotStrategy()

    for candlestick in chart.getPoints():
        strategy.tick(candlestick)


if __name__ == "__main__":
    main(sys.argv[1:])
