import config
import ccxt
from botcandlestick import BotCandlestick
import pandas as pd


class BotChart(object):
    def __init__(self, start, end, exchange, pair, period, backtest=True):
        self.path = config.CONSTS['PATH']
        self.pair = pair
        self.period = period

        self.startTime = start
        self.endTime = end

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
                df = pd.DataFrame(extended_data)

                df.to_csv(config.os.path.join(self.path, 'data/ohlv.csv'))

                for index, row in df.iterrows():
                    self.data.append(
                        BotCandlestick(self.period, row['date'], row['open'],
                                       row['close'], row['high'], row['low'],
                                       row['weightedAverage']))

    def getPoints(self):
        return self.data

    def getCurrentPrice(self):
        # Grab latest ticker data ccxt
        currentValues = self.exchange.fetchTicker(self.pair)
        lastPairPrice = currentValues['last']

        return lastPairPrice
