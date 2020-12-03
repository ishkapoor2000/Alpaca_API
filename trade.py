import requests, json
from sample_config import API_KEY ,API_SECRET_KEY

BASE_URL = 'https://paper-api.alpaca.markets'
ACCOUNT_URL = '{}/v2/account'.format(BASE_URL)
ORDERS_URL = '{}/v2/orders'.format(BASE_URL)
HEADERS = {'APCA-API-KEY' : API_KEY, 'APCA-API-SECRET-KEY' : API_SECRET_KEY}

def get_account():

    r = requests.get(ACCOUNT_URL, headers = HEADERS)

    return json.loads(r.content)

def create_orders(symbol, qty, side, type, time_in_force):

    data = {
        "account_blocked": False,
        "symbol":symbol,
        "qty":qty,
        "side":side,
        "type":type,
        "time_in_force":time_in_force
    }
    r = requests.post(ORDERS_URL, json = data, headers = HEADERS)
    # reminder I need to use json more often!
    return json.loads(r.content)

response = create_orders("AAPL", 100, "buy", "market", "gtc")

print(response)
