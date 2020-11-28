import oandapyV20.endpoints.positions as positions
from connection import Connection

class Position:
  # Load config
  conn = Connection.getInstance()
  accountID = conn.config['ACCOUNT_ID']

  r = positions.OpenPositions(accountID)
  data = conn.API.request(r)['positions']

  def __init__(self, i):
    self.pair = self.data[i]['instrument']
    self.long = self.data[i]['long']
    self.short = self.data[i]['short']

  def is_long(self):
    return True if self.long['units'] != '0' else False
  
  def is_short(self):
    return True if self.short['units'] != '0' else False

