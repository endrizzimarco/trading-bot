from backtesting import Strategy
from indicators import *

# Open position after there has been a big movement
class BigMoves(Strategy):
    n = 10
    threshold = 110
    tpPips = 30

    def init(self):
        self.max = self.I(MAXSEQ, self.data.Close, self.n)
        self.min = self.I(MINSEQ, self.data.Close, self.n)

    def next(self):
        price = self.data.Close[-1]

        if self.position:
            if price < self.data.Close[-2]:
                self.position.close()
        if not self.position:
            if self.max > self.threshold:
                self.buy(size=30000, tp=price + (self.tpPips / 10000))
            if self.min < -self.threshold:
                self.sell(size=30000, tp=price - (self.tpPips / 10000))


# Take profit of next candle after there has been a streak
class Streaks(Strategy):
    n = 4
    streak = 0
    buyStreak = True

    def init(self):
        pass

    def next(self):
        greenCandle = self.data.Open[-1] <= self.data.Close[-1]

        if self.position:
            if greenCandle != self.buyStreak:
                self.position.close()
                self.streak = 0

        if not self.position:
            if greenCandle != self.buyStreak:
                self.buyStreak = not self.buyStreak
                self.streak = 1
            else:
                self.streak += 1

            if self.streak >= self.n:
                self.buy(size=30000) if self.buyStreak else self.sell(size=30000)
                self.timeToDip = True


# Like streaks but you wait a certain amount of candles before dipping
class DippinStreaks(Strategy):
    # To optimize
    n = 4  # n of past candles to consider
    n2 = 2  # Maximum n of candles before taking profit
    threshold = 17  # Need big swing to invest

    streak = 0
    buyStreak = True
    timeToDip = 0

    def init(self):
        self.max = self.I(MAXSEQ, self.data.Close, self.n)
        self.min = self.I(MINSEQ, self.data.Close, self.n)

    def next(self):
        greenCandle = self.data.Open[-1] <= self.data.Close[-1]

        if self.position:
            self.timeToDip += 1

            if greenCandle != self.buyStreak or self.timeToDip >= self.n2:
                self.position.close()
                self.streak = 0
                self.timeToDip = 0

        else:
            if greenCandle != self.buyStreak:
                self.buyStreak = not self.buyStreak
                self.streak = 1
            else:
                self.streak += 1

            if self.streak >= self.n and (
                self.max[-1] >= self.threshold or self.min[-1] <= -self.threshold
            ):
                self.buy(size=30000) if self.buyStreak else self.sell(size=30000)


# https://www.investopedia.com/terms/i/ichimoku-cloud.asp
class Ichimoku(Strategy):
    def init(self):
        self.tenkanSen = self.I(tenkanSen, self.data)
        self.kijunSen = self.I(kijunSen, self.data)
        self.senkouSpanA = self.I(senkouSpanA, self.data)
        self.senkouSpanB = self.I(senkouSpanB, self.data)
        self.chikouSpan = self.I(chikouSpan, self.data)

    def next(self):
        if self.position:
            if (
                self.position.is_long
                and self.tenkanSen[-1] < self.kijunSen[-1]
                and self.data.Close[-1] < self.kijunSen[-1]
            ):
                self.position.close()

            if (
                self.position.is_short
                and self.tenkanSen[-1] > self.kijunSen[-1]
                and self.data.Close[-1] > self.kijunSen[-1]
            ):
                self.position.close()

        else:
            # BUY CONDITIONS
            if (
                self.tenkanSen[-1] > self.kijunSen[-1]
                and self.data.Close[-1] > self.kijunSen[-1]
                and self.chikouSpan[-1] > self.data.Close[-1]
            ):
                self.buy(size=30000)
            # SELL CONDITIONS
            elif (
                self.tenkanSen[-1] < self.kijunSen[-1]
                and self.data.Close[-1] < self.kijunSen[-1]
                and self.chikouSpan[-1] < self.data.Close[-1]
            ):
                self.sell(size=30000)
