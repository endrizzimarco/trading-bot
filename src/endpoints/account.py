import oandapyV20.endpoints.accounts as accounts
from connection import Connection

def getAccount():
  #Load config
  connection = Connection()
  accountID = connection.config['ACCOUNT_ID']
  
  # Request
  r = accounts.AccountSummary(accountID)
  return connection.API.request(r)