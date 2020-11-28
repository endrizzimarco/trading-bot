import oandapyV20.endpoints.accounts as accounts
from connection import Connection

class Account:
  conn = Connection.getInstance()
  accountID = conn.config['ACCOUNT_ID']
  r = accounts.AccountSummary(accountID)
  data = conn.API.request(r)['account']

  def __init__(self):
    self.id = self.data['id']
    self.balance = self.data['balance']
    self.nav = self.data['NAV']
    self.margin = self.data['marginAvailable']
    self.positions = self.data['openPositionCount']

