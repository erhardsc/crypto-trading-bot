import ccxt
from apikeys import APIKeys
import sys
from poloniex import poloniex
import urllib, json
import pprint
from botcandlestick import BotCandlestick

class BotChart(object):
	def __init__(self, exchange, pair, period, backtest=True):
		self.pair = pair
		self.period = period

		self.startTime = 1504224000
		self.endTime = 1506815999

		self.data = []

		if (exchange == "poloniex"):
			apiKey_secret = APIKeys()
			creds = apiKey_secret.poloniex_keys()
			for cred in creds:
				self.key = cred[1]
				self.secret = cred[2]

			self.exchange = ccxt.poloniex()

			self.conn = poloniex(self.key, self.secret)

			if backtest:
				self.exchange.load_markets()
				# Fetch public array of ohlcv data
				poloData = self.exchange.fetch_ohlcv (self.pair, self.period , 0, 0, {"start":self.startTime,"end":self.endTime})

				# Assign OHLCV Candle Stick data
				for ohlcvData in poloData:
					self.time = ohlcvData[0]
					self.openPrice = ohlcvData[1]
					self.highestPrice = ohlcvData[2]
					self.lowestPrice = ohlcvData[3]
					self.closingPrice = ohlcvData[4]
					self.volume = ohlcvData[5]
					if self.time and self.openPrice and self.highestPrice and self.lowestPrice and self.closingPrice and self.volume:
						self.data.append(BotCandlestick(300, self.openPrice, self.closingPrice, self.highestPrice, self.lowestPrice, 0))

				#self.data.append(BotCandlestick(self.period,self.openPrice,self.closingPrice,self.highestPrice,self.lowestPrice))

			# if backtest:
			# 	poloData = self.conn.api_query("returnChartData",{"currencyPair":self.pair,"start":self.startTime,"end":self.endTime,"period":self.period})
			# 	for datum in poloData:
			# 		if (datum['open'] and datum['close'] and datum['high'] and datum['low']):
			# 			self.data.append(BotCandlestick(self.period,datum['open'],datum['close'],datum['high'],datum['low'],datum['weightedAverage']))

		if (exchange == "bittrex"):
			if backtest:
				url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName="+self.pair+"&tickInterval="+self.period+"&_="+str(self.startTime)
				response = urllib.urlopen(url)
				rawdata = json.loads(response.read())

				self.data = rawdata["result"]


	def getPoints(self):
		return self.data

	def getCurrentPrice(self):

		# Grab latest ticker data ccxt
		currentValues = self.exchange.fetchTicker(self.pair)
		lastPairPrice = currentValues['last']

		# currentValues = self.conn.api_query("returnTicker")
		# lastPairPrice = {}
		# lastPairPrice = currentValues[self.pair]["last"]
		return lastPairPrice
