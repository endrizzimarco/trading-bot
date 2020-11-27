import oandapyV20.endpoints.accounts as accounts
from connection import Connection

def getAccount():    
  connection = Connection()
  accountID = connection.config['ACCOUNT_ID']
  r = accounts.AccountSummary(accountID)
  return connection.API.request(r)