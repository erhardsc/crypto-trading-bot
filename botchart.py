import config
import ccxt
from botcandlestick import BotCandlestick


class BotChart(object):
    def __init__(self, exchange, pair, period, backtest=True):
        self.pair = pair
        self.period = period

        self.startTime = 1504224000
        self.endTime = 1506815999

        self.data = []

        if (exchange == "poloniex"):
            # Grab Stored keys
            self.key = config.POLONIEX_CONFIG['key']
            self.secret = config.POLONIEX_CONFIG['secret']
            self.exchange = ccxt.poloniex()

            if backtest:
                self.exchange.load_markets()
                # Fetch public array of ohlcv data
                poloData = self.exchange.fetch_ohlcv(
                    self.pair, self.period, None, None, {
                        "start": self.startTime,
                        "end": self.endTime
                    })
                # Assign OHLCV Candle Stick data
                for ohlcvData in poloData:
                    self.time = ohlcvData[0]
                    self.openPrice = ohlcvData[1]
                    self.highestPrice = ohlcvData[2]
                    self.lowestPrice = ohlcvData[3]
                    self.closingPrice = ohlcvData[4]
                    self.volume = ohlcvData[5]
                    if self.time and self.openPrice and self.highestPrice and self.lowestPrice and self.closingPrice and self.volume:
                        self.data.append(
                            BotCandlestick(
                                86400, self.openPrice, self.closingPrice,
                                self.highestPrice, self.lowestPrice, 0))

    def getPoints(self):
        return self.data

    def getCurrentPrice(self):
        # Grab latest ticker data ccxt
        currentValues = self.exchange.fetchTicker(self.pair)
        lastPairPrice = currentValues['last']

        return lastPairPrice
