import requests
from pprint import pprint
from integrations.utils.request_handler import *

BASE_URL = "https://api.nesatilir.com/api"

api = APIRequestHandler()
api.verbose = True
auth_token = "None"


def get_stock_tracker_productslist() -> dict:
    data = {
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}StockTrackerProductList", "POST", data=data)


pprint(get_stock_tracker_productslist())
