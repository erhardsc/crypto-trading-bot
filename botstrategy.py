from botlog import BotLog
from botindicators import BotIndicators
from bottrade import BotTrade
import pandas as pd
import config


class BotStrategy():
    def __init__(self):
        self.output = BotLog()
        self.path = config.CONSTS['PATH']
        self.prices = []
        self.closes = []  # Needed for Momentum Indicator
        self.trades = []
        self.currentPrice = ""
        self.currentClose = ""
        self.numSimulTrades = 1
        self.indicators = BotIndicators()
        self.movingAVG = []
        self.momentum = []
        self.EMA = []
        self.graph_data = {"Date": [],
                           "Price": [],
                           "MovingAverage": [],
                           "Momentum": []}

    def tick(self, candlestick):
        self.currentPrice = float(candlestick.priceAverage)
        self.movingAVG = self.indicators.movingAverage(self.prices, 15)
        self.momentum = self.indicators.momentum(self.prices, 15)
        # self.EMA = self.indicators.EMA(self.prices, 15)
        self.prices.append(self.currentPrice)
        #self.currentClose = float(candlestick['close'])
        #self.closes.append(self.currentClose)

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

        self.graph_data['Date'].append(candlestick.date.astype(int))
        self.graph_data['Price'].append(self.currentPrice)
        self.graph_data['MovingAverage'].append(self.movingAVG)
        self.graph_data['Momentum'].append(self.momentum)
        # self.graph_data['EMA'].append(self.EMA)
        df = pd.DataFrame(self.graph_data)
        df.to_csv(config.os.path.join(self.path, 'data/indicators.csv'))

    def updateOpenTrades(self):
        for trade in self.trades:
            if (trade.status == "OPEN"):
                trade.tick(self.currentPrice)

    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()
