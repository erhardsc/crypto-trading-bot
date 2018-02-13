from botlog import BotLog
from botindicators import BotIndicators
from bottrade import BotTrade


class BotStrategy():
    def __init__(self):
        self.output = BotLog()
        self.prices = []
        self.closes = []  # Needed for Momentum Indicator
        self.trades = []
        self.currentPrice = ""
        self.currentClose = ""
        self.numSimulTrades = 1
        self.indicators = BotIndicators()

    def tick(self, candlestick):
        self.currentPrice = float(candlestick.priceAverage)
        self.prices.append(self.currentPrice)
        #self.currentClose = float(candlestick['close'])
        #self.closes.append(self.currentClose)

        self.output.log(
            "Price: " + str(candlestick.priceAverage) + "\tMoving Average: " +
            str(self.indicators.movingAverage(self.prices, 15)))

        self.evaluatePositions()
        self.updateOpenTrades()
        self.showPositions()

    def evaluatePositions(self):
        openTrades = []
        movingAVG = self.indicators.movingAverage(self.prices, 15)

        for trade in self.trades:
            if (trade.status == "OPEN"):
                openTrades.append(trade)

        # Make sure NoneType is handled
        if (movingAVG is None):
            movingAVG = 0

        if (len(openTrades) < self.numSimulTrades):
            if (self.currentPrice < movingAVG):
                self.trades.append(BotTrade(self.currentPrice, stopLoss=.0001))

        for trade in openTrades:
            if (self.currentPrice > movingAVG):
                trade.close(self.currentPrice)

    def updateOpenTrades(self):
        for trade in self.trades:
            if (trade.status == "OPEN"):
                trade.tick(self.currentPrice)

    def showPositions(self):
        for trade in self.trades:
            trade.showTrade()
