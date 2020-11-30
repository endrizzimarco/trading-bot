import oandapyV20.endpoints.orders as orders
from connection import Connection
import json

class Order:
    conn = Connection.getInstance()
    accountID = conn.config['ACCOUNT_ID']

    def __init__(self, units, instrument):
      with open('src/orderbody.json', 'r') as f:
        data = json.load(f)
        data['order']['units'] = units
        data['order']['instrument'] = instrument
        self.data = data
      self.units = units

    def create_order(self):
      q = orders.OrderCreate(self.accountID, self.data)
      return self.conn.API.request(q)
