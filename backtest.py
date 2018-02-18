import sys
import getopt
import datetime as dt
from botchart import BotChart
from botstrategy import BotStrategy
import pandas as pd
import config
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import numpy as np


# Testing historical price data.
def main(argv):
    startTime = 0
    endTime = 1506815999
    pair = config.CONSTS['BASE'] + "/" + config.CONSTS['QUOTE']
    exchange = config.CONSTS['EXCHANGE']
    period = config.CONSTS['PERIOD']
    if(not config.CONSTS['VERBOSE']):
        print('Gathering', pair, 'ticker data from', exchange)
    chart = BotChart(startTime, endTime, exchange, pair, period)
    strategy = BotStrategy()

    for candlestick in chart.getPoints():
        strategy.tick(candlestick)

    print("Finished gathing data")
    # graph_data(pair)


def graph_data(pair):
    path = config.CONSTS['PATH']
    plt.title(pair)
    df = pd.read_csv(path + "/data/indicators.csv", parse_dates=True, infer_datetime_format=True, index_col=0)
    date = df["Date"]
    price = df["Price"]
    dateconv = mdate.epoch2num(date)
    fig, ax = plt.subplots()
    ax.plot_date(dateconv, price)
    date_fmt = '%d-%m-%y %H:%M:%S'
    date_formatter = mdate.DateFormatter(date_fmt)
    ax.xaxis.set_major_formatter(date_formatter)

    fig.autofmt_xdate()

    plt.show()


if __name__ == "__main__":
    main(sys.argv[1:])
