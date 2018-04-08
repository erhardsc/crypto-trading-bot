from botchart import BotChart
from botstrategy import BotStrategy
from config import CONFIG
import sys


# Testing historical price data.
def main(argv):
    startTime = CONFIG["START"]
    endTime = CONFIG["END"]
    # pair = CONFIG['BASE'] + "/" + CONFIG['QUOTE']
    exchange = CONFIG['EXCHANGE']
    period = CONFIG['PERIOD']
    pairs = CONFIG['PAIRS']

    for pair in pairs:
        if(not CONFIG['VERBOSE']):
            print('Gathering', pair, 'ticker data from', exchange)

        chart = BotChart(startTime, endTime, exchange, pair, period)
        strategy = BotStrategy(pair)

        for candlestick in chart.getPoints():
            strategy.tick(candlestick)

        print("Finished gathing data for " + pair + "\n")

if __name__ == "__main__":
    main(sys.argv[1:])
