
from connection import Connection
from endpoints.account import Account
from endpoints.position import Position
from endpoints.instrument import Instrument

account = Account()
# Print account details
print(
  f'**** Account ****\n\n'
  f"Account ID: {account.id}\n"
  f"Balance: {account.balance}\n"
  f"Net Asset Value: {account.nav}\n"
  f"Margin available: {account.margin}\n"
  f"Opened positions: {account.positions}\n\n"
  )

# Print open positions
print(f'**** Open Positions ****\n')
for n in range(len(Position.data)):
  position = Position(n)
  print(f"{n+1}: {position.pair}")

  if position.is_long():
    print(f"  Long: {position.long['units']} units, {position.long['unrealizedPL']} PL\n\n")
  if position.is_short():
      print( f"  Short: {position.long['units']} units, {position.short['unrealizedPL']} PL\n\n")


# Print values of currency pairs an hour ago vs now
print(f'**** 1h price difference ****\n')
for pair in Instrument.pairs.split(','):
  candles = Instrument(pair)

  print(
    f'{pair}:\n'
    f" {candles.time(candles.last)}, {candles.price(candles.last)}\n"
    f" {candles.time(candles.curr)}, {candles.price(candles.curr)}\n"
  )

