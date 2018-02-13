import config
import ccxt
import json
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

                extended_data = self.exchange.last_json_response
                for parsed_data in extended_data:
                    if (parsed_data['open'] and parsed_data['close']
                            and parsed_data['high'] and parsed_data['low']):
                        self.data.append(
                            BotCandlestick(self.period, parsed_data['open'],
                                           parsed_data['close'],
                                           parsed_data['high'],
                                           parsed_data['low'],
                                           parsed_data['weightedAverage']))
                
    def getPoints(self):
        return self.data

    def getCurrentPrice(self):
        # Grab latest ticker data ccxt
        currentValues = self.exchange.fetchTicker(self.pair)
        lastPairPrice = currentValues['last']

        return lastPairPrice
