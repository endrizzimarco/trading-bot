
from endpoints.account import Account
from endpoints.position import Position
from endpoints.instrument import Instrument
from endpoints.pricing import Pricing
from endpoints.order import Order
import configparser
import schedule
import time

# Load config
config = configparser.ConfigParser()
config.read('config.ini')
config = config['STRATEGY']

PAIRS = config['INSTRUMENTS'].split(',')
RATE = int(config['PIP_DIFF'])
UNITS = int(config['UNITS'])

account = Account()
# Print account details
print(
  f'****** Account ******\n\n'
  f'Account ID: {account.id}\n'
  f'Balance: {account.balance}\n'
  f'Net Asset Value: {account.nav}\n'
  f'Margin available: {account.margin}\n'
  f'Opened positions: {account.positions}\n\n'
  )

# Print open positions
print(f'****** Open Positions ******\n')
if len(Position.data) == 0:
  print('No positions are currently opened\n\n')

for n in range(len(Position.data)):
  position = Position(n)
  print(f'{n+1}: {position.pair}')

  if position.is_long():
    print(f"  Long: {position.long['units']} units, {position.long['unrealizedPL']} PL\n\n")
  if position.is_short():
      print(f"  Short: {position.long['units']} units, {position.short['unrealizedPL']} PL\n\n")

def job():
  # Print values of currency pairs an hour ago vs now
  print(f'****** 1h price difference ******\n')
  for pair in PAIRS:
    candles = Instrument(pair)
    max, min = candles.max_min_subsequence()

    print(
      f'{pair}:\n'
      f'  {candles.lastTime}, {candles.lastPrice}\n'
      f'  {candles.currTime}, {candles.currPrice}\n'
      f'  Biggest price increase: {max} pips\n'
      f'  Biggest price decrease: {min} pips'
    )

    pairInfo = Pricing(pair)

    if pairInfo.is_tradeable() and pairInfo.unitsAvailable > UNITS:
      if not Position.is_opened(pair):
        units = 0
        if max > RATE: 
          units = UNITS
        elif min < -RATE:
          units = -UNITS
        if units:
          order = Order(str(units), pair)
          order.create_order()
          print(f'-> Order created for {pair} for {order.units} units\n')
        else:
          print('-> No good movement\n')
      else: 
        print('-> A position is already opened for this pair\n')
    else:
      print('-> Pair not tradeable at the moment\n')

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)