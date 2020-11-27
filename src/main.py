
from connection import Connection
from endpoints import account
import json

print("RESPONSE:\n{}".format(json.dumps(account.getAccount(), indent=2)))