import oandapyV20.endpoints.instruments as instruments
from connection import Connection

class Instrument:
  conn = Connection.getInstance()
  params = {"count": 60, "granularity": 'M1'}

  def __init__(self, instrument):
    self.q = instruments.InstrumentsCandles(instrument, self.params)
    self.prices = self.conn.API.request(self.q)['candles']
    self.currPrice = self.prices[0]['mid']['o']
    self.lastPrice = self.prices[-1]['mid']['o']
    self.currTime = self.prices[0]['time'][11:16]
    self.lastTime = self.prices[-1]['time'][11:16]

  def max_min_subsequence(self):
    openPrices = [float(price['mid']['o']) for price in self.prices]
    priceChange = [round(openPrices[i+1]-openPrices[i], 5) for i in range(len(openPrices)-1)]
    maxSoFar = 0
    minSoFar = 0
    maxToHere = 0
    minToHere = 0

    for i in range(len(priceChange)):
      maxToHere += priceChange[i]
      minToHere += priceChange[i]
      if maxToHere < 0:
        maxToHere = 0
      if minToHere > 0:
        minToHere = 0
      if maxSoFar < maxToHere:
        maxSoFar = maxToHere
      if minSoFar > minToHere:
        minSoFar = minToHere

    return int((maxSoFar*10**5)), int((minSoFar*10**5))
