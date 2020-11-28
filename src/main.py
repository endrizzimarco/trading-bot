
from connection import Connection
from endpoints import account, position, instrument, order


account = account.getAccount()['account']

print(
  f'**** Account ****\n\n'
  f"Account ID: {account['id']}\n"
  f"Balance: {account['balance']}\n"
  f"Net Asset Value: {account['NAV']}\n"
  f"Margin available: {account['marginAvailable']}\n"
  f"Opened positions: {account['openPositionCount']}\n\n"
  )

positions = position.getOpenPositions()['positions']

print(f'**** Open Positions ****\n')
for n, position in enumerate(positions):
  print(f"{n+1}: {position['instrument']}")
  if position['long']['units'] != '0': 
    print(
      f"  Long: {position['long']['units']} units, {position['long']['unrealizedPL']} PL\n"
    )
  if position['short']['units'] != '0': 
      print(
      f"  Short: {position['short']['units']} units, {position['short']['unrealizedPL']} PL\n"
    )
