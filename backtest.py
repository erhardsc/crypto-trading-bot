import sys
import getopt
import datetime as dt
from botchart import BotChart
from botstrategy import BotStrategy
import pandas as pd
import config
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np


# Testing historical price data.
def main(argv):
    startTime = 1502224000
    endTime = 1506815999
    pair = "ETH/BTC"
    chart = BotChart(startTime, endTime, "poloniex", pair, "1d")
    strategy = BotStrategy()

    for candlestick in chart.getPoints():
        strategy.tick(candlestick)

    graph(pair)


def graph(pair):
    path = config.CONSTS['PATH']
    plt.title(pair)
    df = pd.read_csv(path + "/data/indicators.csv", parse_dates=True, infer_datetime_format=True, index_col=0)
    date = df["Date"]
    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)
    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
