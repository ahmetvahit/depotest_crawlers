import requests
from pprint import pprint
from integrations.utils.request_handler import *

BASE_URL = "https://api.nesatilir.com/api"

api = APIRequestHandler()
api.verbose = True
auth_token = "None"


def get_retail_arbitrage_products(cat_id: str, country: str = "usa", amazon_country: str = "USA") -> dict:
    data = {
        'is_favorite': 0,
        'page': 0,
        'country': country,
        'cat': [
            cat_id,
            '',
        ],
        'cattype': '1',
        'prod': {
            'all': 1,
        },
        'include': '',
        'orderby': 'FarkYuzde',
        'ordertype': 'DESC',
        'displayrow': 25,
        'Token': auth_token,
        'DeviceType': 0,
        'ArbitrageType': '',
        'SellerTypes': 'all',
        'BadgesTypes': 'all',
        'AmazonCountry': amazon_country,
    }
    return api._request(f"{BASE_URL}/v1/GetTYRetailArbitrageProducts", "POST", data=data)


pprint(get_retail_arbitrage_products(1071))
