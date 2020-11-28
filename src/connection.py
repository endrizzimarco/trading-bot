from oandapyV20 import API
import configparser

class Connection:
  __instance = None
  API = None
  config = {}

  @staticmethod
  def getInstance():
    """ Static access method """
    if Connection.__instance == None:
      Connection()
    return Connection.__instance


  def __init__(self):
    """ Virtually private constructor """
    if Connection.__instance != None:
      raise Exception("This class is a singleton")
    else:
      Connection.__instance = self

      config = configparser.ConfigParser()
      config.read('config.ini')
      mode = config['ENV']['MODE']
      self.config = config[mode]

      enviroment = self.config['TYPE']
      access_token = self.config['AUTH_TOKEN']
      self.API = API(access_token, enviroment)