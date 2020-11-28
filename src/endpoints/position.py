import oandapyV20.endpoints.positions as positions
from connection import Connection

def getOpenPositions():
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']

    # Request
    r = positions.OpenPositions(accountID)
    return connection.API.request(r)

