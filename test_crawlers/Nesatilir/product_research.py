import requests
from pprint import pprint
from integrations.utils.request_handler import *

BASE_URL = "https://api.nesatilir.com/api"

api = APIRequestHandler()
api.verbose = True
auth_token = "None"


def get_product_resarch(category_id: str) -> dict:
    data = {
        'is_favorite': 0,
        'page': 0,
        'country': '',
        'cat': [
            category_id,
            '',
        ],
        'cattype': '1',
        'prod': {
            'all': 1,
        },
        'includev2': [],
        'orderby': 'Last30DaySales',
        'ordertype': 'DESC',
        'displayrow': 25,
        'Token': auth_token,
        'DeviceType': 0,
        'ArbitrageType': '',
        'SellerTypes': 'all',
        'BadgesTypes': 'all',
        'AmazonCountry': 'US',
    }
    return api._request(f"{BASE_URL}/v1/TYGetProducts", "POST", data=data)


pprint(get_product_resarch(403))
