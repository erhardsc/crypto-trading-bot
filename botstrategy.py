import config
from botlog import BotLog
from botindicators import BotIndicators
from bottrade import BotTrade
import pandas as pd


class BotStrategy():
    def __init__(self, pair):
        if(not config.CONFIG["VERBOSE"]):
            print("Calculating indicators")
        self.pair = pair
        self.output = BotLog()
        self.path = config.CONFIG['PATH']
        self.prices = []
        self.closes = []
        self.trades = []
        self.movingAVG = []
        self.momentum = []
        self.RSI = []
        self.currentPrice = ""
        self.currentClose = ""
        self.numSimulTrades = 1
        self.indicators = BotIndicators()
        self.graph_data = {"date": [],
                           "movingAverage": [],
                           "momentum": [],
                           "RSI": []
                           }

    def tick(self, candlestick):
        self.currentPrice = float(candlestick.priceAverage)
        self.currentClose = float(candlestick.close)
        self.movingAVG = self.indicators.movingAverage(self.prices, 15)
        self.momentum = self.indicators.momentum(self.closes, 15)
        self.RSI = self.indicators.RSI(self.prices, 15)
        self.MACD = self.indicators.MACD(self.prices)
        self.prices.append(self.currentPrice)
        self.closes.append(self.currentClose)
        self.output.log("Price: " + str(candlestick.priceAverage) +
                        "\tMoving Average: " + str(self.movingAVG))

        self.evaluatePositions(candlestick)
        self.updateOpenTrades()
        self.showPositions()

    def evaluatePositions(self, candlestick):
        openTrades = []

        for trade in self.trades:
            if (trade.status == "OPEN"):
                openTrades.append(trade)

        # Make sure NoneType is handled
        if (self.movingAVG is None):
            self.movingAVG = 0

        if (len(openTrades) < self.numSimulTrades):
            if (self.currentPrice < self.movingAVG):
                self.trades.append(BotTrade(self.currentPrice, stopLoss=.0001))

        for trade in openTrades:
            if (self.currentPrice > self.movingAVG):
                trade.close(self.currentPrice)

        self.graph_data['date'].append(candlestick.date.astype(int))
        self.graph_data['movingAverage'].append(self.movingAVG)
        self.graph_data['momentum'].append(self.momentum)
        self.graph_data['RSI'].append(self.RSI)

        df = pd.DataFrame(self.graph_data)
        df.to_csv(config.os.path.join(self.path, 'data/' + self.pair.replace('/','-') + "/" + 'indicators.csv'))

    def updateOpenTrades(self):
        for trade in self.trades:
            if (trade.status == "OPEN"):
                trade.tick(self.currentPrice)

    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()
