import oandapyV20.endpoints.pricing as pricing
from connection import Connection

class Pricing:
  # Load config
  conn = Connection.getInstance()
  accountID = conn.config['ACCOUNT_ID']

  def __init__(self, instrument):
    self.q = pricing.PricingInfo(self.accountID, {"instruments": instrument})
    self.data = self.conn.API.request(self.q)['prices'][0]
    self.unitsAvailable = float(self.data['unitsAvailable']['default']['long'])

  def is_tradeable(self):
    return True if self.data['tradeable'] == 'True' else False
