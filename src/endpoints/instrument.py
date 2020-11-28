import oandapyV20.endpoints.instruments as instruments
from connection import Connection

def getPrices(instrument):    
  connection = Connection()

  # Request
  params = {"count": 60, "granularity": M1}
  r = instruments.InstrumentsCandles(instrument, params)
  return connection.API.request(r)