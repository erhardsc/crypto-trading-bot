import sys, getopt
import time

from botchart import BotChart
from botstrategy import BotStrategy
from botlog import BotLog
from botcandlestick import BotCandlestick

# Testing live price data
def main(argv):
	#chart = BotChart("poloniex","BTC_LTC",300,False)
	chart = BotChart("poloniex","BTS/BTC","1d",False)

	strategy = BotStrategy()

	candlesticks = []
	developingCandlestick = BotCandlestick()

	while True:
		try:
			developingCandlestick.tick(chart.getCurrentPrice())
		except urllib2.URLError:
			time.sleep(int(30))
			developingCandlestick.tick(chart.getCurrentPrice())

		if (developingCandlestick.isClosed()):
			candlesticks.append(developingCandlestick)
			strategy.tick(developingCandlestick)
			developingCandlestick = BotCandlestick()

		time.sleep(int(30))

if __name__ == "__main__":
	main(sys.argv[1:])
