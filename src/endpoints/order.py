import oandapyV20.endpoints.orders as orders
from connection import Connection
import json

def createOrder(units, instrument):
    # Load config
    connection = Connection()
    accountID = connection.config['ACCOUNT_ID']
    
    # Load json
    with open('orderbody.json', 'r') as f:
        data = json.load(f)
        
    # Set units and instrument
    data['order']['units'] = units
    data['order']['instrument'] = instrument
    print(f'Create Order Request: {data}\n')
    
    # Request
    r = orders.OrderCreate(accountID, data)
    return connection.API.request(r)