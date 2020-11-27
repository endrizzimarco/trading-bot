from oandapyV20 import API
import configparser

class Connection:
  config = {}
  API = None

  def __init__(self):
    config = configparser.ConfigParser()
    config.read('config.ini')
    mode = config['ENV']['MODE']
    Connection.config = config[mode]

    enviroment = Connection.config['TYPE']
    access_token = Connection.config['AUTH_TOKEN']
    Connection.API = API(access_token, enviroment)
