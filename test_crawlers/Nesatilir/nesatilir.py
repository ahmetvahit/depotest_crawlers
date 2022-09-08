import requests
from pprint import pprint
from integrations.utils.request_handler import *

BASE_URL = "https://api.nesatilir.com/api"

api = APIRequestHandler()
api.verbose = True
auth_token = "None"


def get_favorite_products(category_id: str, platfrom_id: str = "TY") -> dict:
    data = {
        'siteId': platfrom_id,
        'categoryId': category_id,
        'Token': auth_token,
    }
    return api._request(f"{BASE_URL}/v1/GetTop100Analysis", "POST", data=data)


pprint(get_favorite_products(3494))
