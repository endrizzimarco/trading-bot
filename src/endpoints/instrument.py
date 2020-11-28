import oandapyV20.endpoints.instruments as instruments
from connection import Connection

class Instrument:
  conn = Connection.getInstance()
  params = {"count": 60, "granularity": 'M1'}
  pairs = conn.config['INSTRUMENTS']

  def __init__(self, instrument):
    self.r = instruments.InstrumentsCandles(instrument, self.params)
    self.prices = self.conn.API.request(self.r)['candles']
    self.curr = self.prices[0]
    self.last = self.prices[-1]

  def time(self, candle):
    return candle['time'][11:16]

  def price(self, candle):
    return candle['mid']['o']
