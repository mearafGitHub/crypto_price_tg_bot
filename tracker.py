import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import datetime


# https://pythonguides.com/json-data-in-python/

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
bl_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
coin_gecko_cardano_api = 'https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=false'


def get_cardano_price():
    try:
        resp = requests.get(coin_gecko_cardano_api)
        cardano_data = json.loads(resp.text)
        cardano_price = cardano_data['cardano']['usd']
        cardano_volume = cardano_data['cardano']['usd_24h_vol']
        cardano_market_cap = cardano_data['cardano']['usd_market_cap']
        print(cardano_data)
        print("ADA price: ", cardano_price)
        print("Volume: ", cardano_volume)
        print("Market Cap: ", cardano_market_cap)
        return cardano_data

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
