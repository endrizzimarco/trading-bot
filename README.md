# trading-bot
Simple trading bot using OANDA v20 API that tries to catch big trends by opening a position when there's been a movement of a set amount of pips in the last hour.

## Setup
### Install dependencies
Setup your python virtual enviroment. [How to set up.](https://docs.python.org/3/tutorial/venv.html)

`$ pip3 install -r requirements.txt` 
  
### Token
This project requires an API key from [OANDA](https://developer.oanda.com/). Get your token [here](https://developer.oanda.com/rest-live-v20/introduction/).

### config.ini format
```
[ENV]
MODE=TEST

#Practice account auth
[TEST]
TYPE=practice
ACCOUNT_ID=xxx-xxx-xxxxxxxx-xxx
AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx

#Real account auth
[REAL]
TYPE=live
ACCOUNT_ID=xxx-xxx-xxxxxxxx-xxx
AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxx

#Investing strategy
[STRATEGY]
INSTRUMENTS=EUR_USD,EUR_GBP,GBP_USD,CAD_CHF # Currency pairs to trade on
PIP_DIFF=200 # Invest if currency pair moves 200 pips in either direction
UNITS=15000 # Currency units to invest per trade
```
## Run
### Direct run
`$ python3 src/main.py`

### Run in background
`$ nohup python3 src/main.py &`





