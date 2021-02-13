import oandapyV20.endpoints.instruments as instruments
import pandas as pd
from connection import Connection

class Instrument:
  conn = Connection.getInstance()
  
  def __init__(self, instrument, params):
    self.q = instruments.InstrumentsCandles(instrument, params)
    self.prices = self.conn.API.request(self.q)['candles']
    self.df = self.__to_df()


  def __to_df(self):
    if not(self.prices):
      return None

    df = pd.DataFrame.from_dict(self.prices)
    df.drop('complete', axis=1, inplace=True, errors='ignore')

    df['time'] = df['time'].astype('datetime64[s]')
    df = df.set_index('time').rename_axis(None)

    df = pd.concat([df.drop(['mid'], axis=1), df['mid'].apply(pd.Series)], axis=1)
    df.columns = ['Volume', 'Open', 'High', 'Low', 'Close']
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

    df = df.apply(pd.to_numeric) 
    
    return df


