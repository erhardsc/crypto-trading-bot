from botcandlestick import BotCandlestick
import ccxt
import config
from keys import POLONIEX_CONFIG
import pandas as pd
import util as util


class BotChart(object):
    def __init__(self, start, end, exchange, pair, period, backtest=True):
        self.path = config.CONFIG['PATH']
        self.pair = pair
        self.pairs_dir = "data/" + self.pair.replace('/','-')
        self.period = period

        self.startTime = start
        self.endTime = end

        self.data = []

        if (exchange == "poloniex"):
            # Grab Stored keys
            self.key = POLONIEX_CONFIG['key']
            self.secret = POLONIEX_CONFIG['secret']
            self.exchange = ccxt.poloniex()

            if backtest:
                self.exchange.load_markets()
                # Fetch public array of ohlcv data
                self.exchange.fetch_ohlcv(
                    self.pair, self.period, None, None, {
                        "start": self.startTime,
                        "end": self.endTime
                    })
                extended_data = self.exchange.last_json_response
                df = pd.DataFrame(extended_data)

                util.create_dir(self.pairs_dir)

                df.to_csv(util.os.path.join(self.path, self.pairs_dir + "/" + 'candlesticks.csv'))

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
